// Renders index.html frame-by-frame and muxes with cadie-audio.wav -> cadie.mp4
// usage: node render.js [fps=30] [times...]   (times => stills only, for checking)
const path = require('path'), { spawn } = require('child_process'), fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright-core');
const dir = __dirname, fps = +(process.argv[2] || 30), stills = process.argv.slice(3).map(Number);
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME, args: ['--force-color-profile=srgb', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on('console', m => console.log('page:', m.text())); page.on('pageerror', e => console.log('ERR', e.message));
  await page.goto('file://' + path.join(dir, 'index.html') + '?capture');
  await page.waitForFunction('window.__ready === true', null, { timeout: 60000 });
  const shot = () => page.locator('#stage').screenshot({ type: stills.length ? 'png' : 'jpeg', quality: stills.length ? undefined : 95 });
  if (stills.length) {
    fs.mkdirSync(path.join(dir, 'stills'), { recursive: true });
    for (const t of stills) { await page.evaluate(t => window.renderAt(t), t); fs.writeFileSync(path.join(dir, 'stills', `t${t.toFixed(2)}.png`), await shot()); }
  } else {
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-i', path.join(dir, 'cadie-audio.wav'),
      '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', path.join(dir, 'cadie.mp4')], { stdio: ['pipe', 'inherit', 'inherit'] });
    const N = Math.round(20 * fps);
    for (let i = 0; i < N; i++) { await page.evaluate(t => window.renderAt(t), i / fps); const b = await shot(); if (!ff.stdin.write(b)) await new Promise(r => ff.stdin.once('drain', r)); if (i % 60 === 0) console.log('frame', i, '/', N); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await browser.close();
})();
