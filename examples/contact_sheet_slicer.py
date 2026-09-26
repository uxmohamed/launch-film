import json, sys, os, re
from PIL import Image, ImageDraw
S = os.path.dirname(os.path.abspath(__file__))
secs = {s['name']: s for s in json.load(open(f'{S}/secs.json'))}
def safe(n): return re.sub(r'[^A-Za-z0-9]+', '_', n).strip('_')
os.makedirs(f'{S}/sheets', exist_ok=True)
for fn in sorted(os.listdir(f'{S}/ref')):
    name = fn[:-4]
    key = next((k for k in secs if safe(k) == safe(name) or k == name), None)
    if not key: print('no match', name); continue
    out = f'{S}/sheets/{safe(key)}'
    if os.path.isdir(out): continue
    os.makedirs(out)
    im = Image.open(f'{S}/ref/{fn}').convert('RGB')
    fr = secs[key]['frames']
    fr = sorted(fr, key=lambda f: (float(f[3]), float(f[2])))
    fw, fh = int(float(fr[0][4])), int(float(fr[0][5]))
    sc = 360 / fw; tw, th = 360, int(fh * sc)
    per = 20; cols = 5
    for k in range(0, len(fr), per):
        part = fr[k:k+per]; rows = (len(part) + cols - 1) // cols
        sheet = Image.new('RGB', (cols*tw + (cols-1)*6, rows*(th+22)), (255, 255, 255)); d = ImageDraw.Draw(sheet)
        for i, f in enumerate(part):
            x, y = float(f[2]), float(f[3])
            crop = im.crop((int(x), int(y), int(x)+fw, int(y)+fh)).resize((tw, th))
            px, py = (i % cols)*(tw+6), (i // cols)*(th+22)
            sheet.paste(crop, (px, py+20)); d.text((px+2, py+4), f'#{k+i+1} ({f[1]})', fill=(220, 0, 0))
        sheet.save(f'{out}/sheet_{k//per+1:02d}.jpg', quality=88)
    print(key, len(fr), 'frames ->', (len(fr)+per-1)//per, 'sheets')
