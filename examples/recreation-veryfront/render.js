// node render.js [fps] [times...] — full film → relay-film.mp4, or stills
const path = require('path'), { spawn } = require('child_process'), fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright-core');
const dir = __dirname, fps = +(process.argv[2] || 30), stills = process.argv.slice(3).map(Number), DUR = 30.5;
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME, args: ['--force-color-profile=srgb', '--font-render-hinting=none', '--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => console.log('ERR', e.message)); page.on('console', m => m.type() === 'error' && console.log('console:', m.text()));
  await page.goto('file://' + path.join(dir, 'relay-film.html') + '?capture');
  await page.waitForFunction('window.__ready === true', null, { timeout: 60000 });
  const shot = (type) => page.locator('#stage').screenshot({ type, quality: type === 'jpeg' ? 95 : undefined });
  if (stills.length) {
    fs.mkdirSync(path.join(dir, 'stills'), { recursive: true });
    for (const t of stills) { await page.evaluate(t => window.renderAt(t), t); fs.writeFileSync(path.join(dir, 'stills', `t${t.toFixed(2).padStart(5, '0')}.png`), await shot('png')); }
  } else {
    const wav = path.join(dir, 'relay-audio.wav'), audio = fs.existsSync(wav) ? ['-i', wav, '-c:a', 'aac', '-b:a', '256k', '-shortest'] : [];
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', ...audio, '-c:v', 'libx264', '-preset', 'slow', '-crf', '15', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path.join(dir, 'relay-film.mp4')], { stdio: ['pipe', 'inherit', 'inherit'] });
    const N = Math.round(DUR * fps);
    for (let i = 0; i < N; i++) { await page.evaluate(t => window.renderAt(t), i / fps); const b = await shot('jpeg'); if (!ff.stdin.write(b)) await new Promise(r => ff.stdin.once('drain', r)); if (i % 150 === 0) console.log('frame', i, '/', N); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
