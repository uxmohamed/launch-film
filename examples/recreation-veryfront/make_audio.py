"""Relay film: score and sound design (30.5 s, 48 kHz stereo).

Clean, bright product score at 120 BPM (one beat = the film's 0.5 s pulse), D major:
soft plucks, an airy pad, a light kick and shaker. It drops out under the 8x zoom punch,
lands a hit on the send press, and resolves on the logo. It ends where it began so the film loops.
Every SFX time below comes from relay-film.html.
Usage: python3 make_audio.py  ->  relay-audio.wav
"""
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000; DUR = 30.5; N = int(SR*DUR)
rng = np.random.default_rng(21)

class Bus:
    def __init__(s): s.L = np.zeros(N); s.R = np.zeros(N)
    def add(s, sig, t, pan=0.0, gain=1.0):
        i = int(round(t*SR))
        if i >= N or len(sig) == 0: return
        sig = sig[:N-i]*gain; a = (np.clip(pan, -1, 1)+1)*np.pi/4
        s.L[i:i+len(sig)] += sig*np.cos(a); s.R[i:i+len(sig)] += sig*np.sin(a)
music, drums, sfx = Bus(), Bus(), Bus()
def sos(k, f, o=2): return butter(o, f, k, fs=SR, output='sos')
def lp(x, f, o=2): return sosfilt(sos('low', f, o), x)
def hp(x, f, o=2): return sosfilt(sos('high', f, o), x)
def bp(x, lo, hi, o=2): return sosfilt(sos('band', [lo, hi], o), x)
def tt(d): return np.arange(int(d*SR))/SR
def hz(n):
    m = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11,'Bb':10}
    return 440*2**((m[n[:-1]] + 12*(int(n[-1])+1) - 69)/12)
def fade(x, fi=.002, fo=.01):
    n = len(x); a = min(int(fi*SR), n); b = min(int(fo*SR), n)
    x[:a] *= np.linspace(0, 1, a); x[n-b:] *= np.linspace(1, 0, b); return x
def mix(*xs):
    n = max(len(x) for x in xs); o = np.zeros(n)
    for x in xs: o[:len(x)] += x
    return o

# ---------- instruments ----------
def pluck(f, d=.8, tone=4200):
    t = tt(d)
    x = np.sin(2*np.pi*f*t) + .45*np.sin(2*np.pi*2*f*t) + .18*np.sin(2*np.pi*3*f*t)
    return fade(lp(x*np.exp(-t/.2)*np.minimum(1, t/.002), tone), .001, .08)
def bell(f, d=1.8):
    t = tt(d)
    x = np.sin(2*np.pi*f*t)*np.exp(-t/.8) + .3*np.sin(2*np.pi*2.76*f*t)*np.exp(-t/.22) + .1*np.sin(2*np.pi*5.4*f*t)*np.exp(-t/.08)
    return fade(x*np.minimum(1, t/.001), .001, .2)
def pad(freqs, dur, a=.5, r=1.2, cut=3000, hpf=200):
    n = int((dur+r)*SR); t = np.arange(n)/SR; x = np.zeros(n)
    for f in freqs:
        for d in (-.06, 0, .06):
            ff = f*2**(d/12); ph = rng.uniform(0, 6.28)
            for h, g in ((1,1),(2,.35),(3,.15)): x += g*np.sin(2*np.pi*ff*h*t + ph*h)
    x = hp(lp(x, cut), hpf)/(len(freqs)*3)
    return x*np.minimum(1, t/a)*np.where(t > dur, np.exp(-(t-dur)/(r/3)), 1)
def bass(f, d=.4):
    t = tt(d); x = np.sin(2*np.pi*f*t) + .3*np.sin(2*np.pi*2*f*t)
    return fade(lp(x*np.exp(-t/.28), 500), .003, .05)
def kick():
    t = tt(.3); f = 52 + 110*np.exp(-t/.025)
    return fade(np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/.09) + bp(rng.standard_normal(len(t)), 2000, 6000)*np.exp(-t/.003)*.18, .0005, .04)
def shaker(g=1):
    t = tt(.07); return hp(rng.standard_normal(len(t)), 6500)*np.sin(np.pi*t/.07)**2*.4*g
def snap():
    t = tt(.2); x = np.zeros(len(t))
    for k, o in enumerate((0, .008, .016)):
        i = int(o*SR); m = len(t)-i; x[i:] += bp(rng.standard_normal(m), 1200, 5000)*np.exp(-np.arange(m)/SR/(.01 if k < 2 else .05))
    return x*.5

# ---------- sfx ----------
def tick(f=2600, g=1):
    t = tt(.04); return (np.sin(2*np.pi*f*t)*np.exp(-t/.006)*.6 + bp(rng.standard_normal(len(t)), 3000, 9000)*np.exp(-t/.0018)*.4)*g
def key(g=1):
    t = tt(.03); return (bp(rng.standard_normal(len(t)), 1500, 7000)*np.exp(-t/.003) + np.sin(2*np.pi*rng.uniform(1000, 1500)*t)*np.exp(-t/.005)*.3)*g
def click():
    t = tt(.05); a = bp(rng.standard_normal(len(t)), 2000, 8000)*np.exp(-t/.0015); b = np.zeros(len(t)); i = int(.02*SR); b[i:] = a[:len(t)-i]*.6
    return (a + b)*.7 + np.sin(2*np.pi*200*t)*np.exp(-t/.008)*.3
def pop(f0=500, f1=1000, d=.09):
    t = tt(d); f = f1 + (f0-f1)*np.exp(-t/.015)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/.025)*np.minimum(1, t/.001)
def whoosh(d, lo=300, hi=6000, peak=.7, rev=False):
    t = tt(d); p = t/d; x = rng.standard_normal(len(t)); bands = np.geomspace(lo, hi, 7); out = np.zeros(len(t))
    for k in range(6):
        c = (1-p) if rev else p; out += bp(x, bands[k], bands[k+1])*np.exp(-((c - k/5)**2)/.03)
    return out*np.where(p < peak, (p/peak)**2, np.exp(-(p-peak)/((1-peak)*.35 + 1e-3)))*.5
def swell(d, lo=200, hi=2500):
    t = tt(d); return bp(rng.standard_normal(len(t)), lo, hi)*(t/d)**2*np.exp(-np.maximum(0, t - d*.85)/.05)*.5
def thump(f=60, d=.4):
    t = tt(d); ff = f + 90*np.exp(-t/.03); return np.sin(2*np.pi*np.cumsum(ff)/SR)*np.exp(-t/.12)
def riser(d, f0=300, f1=2400):
    t = tt(d); f = f0*(f1/f0)**(t/d)
    return (np.sin(2*np.pi*np.cumsum(f)/SR)*.3 + hp(rng.standard_normal(len(t)), 2500)*(t/d)**2*.4)*(t/d)**1.5
def shimmer(d):
    t = tt(d); x = np.zeros(len(t))
    for f in (2349, 2960, 3520): x += np.sin(2*np.pi*f*t + rng.uniform(0, 6))*(.5 + .5*np.sin(2*np.pi*3*t + f))
    return x*np.sin(np.pi*t/d)*.08

# ---------- harmony: D major, bright ----------
CH = {'D':['D4','F#4','A4','C#5'],'Bm':['B3','D4','F#4','A4'],'G':['G3','B3','D4','F#4'],'A':['A3','C#4','E4','G4'],'Em':['E4','G4','B4','D5']}
ROOT = {'D':'D2','Bm':'B1','G':'G1','A':'A1','Em':'E2'}
PROG = ['D','Bm','G','A']
T0 = 4.0; BAR = 2.0; BEAT = .5

# open: the sphere arrives; soft bell + air pad (mirrored at the end for the loop)
music.add(pad([hz(n) for n in ['D4','A4','E5']], 3.4, a=.4, r=1.2, cut=2400), 0.0, gain=.3)
for i, n in enumerate(['A5','D6']): music.add(bell(hz(n), 1.6), .05 + i*.08, pan=(i-.5)*.4, gain=.08)
music.add(pluck(hz('F#5'), .9), .6, gain=.14); music.add(pluck(hz('A5'), .9), .75, gain=.12)

# groove 4.0 → 28.0; drops out under the zoom punch (22.1–22.9)
t = T0; kicks = []
while t < 28.0 - 1e-6:
    k = int(round((t - T0)/BAR)); ch = PROG[k % 4]; fr = [hz(n) for n in CH[ch]]
    music.add(pad(fr, BAR, a=.25, r=.7, cut=3000), t, gain=.3)
    for j, idx in enumerate([0, 2, 1, 3, 2, 1, 3, 2]):
        tj = t + j*.25
        if 22.05 <= tj < 22.9: continue
        music.add(pluck(fr[idx]*2 if j % 2 == 0 else fr[idx], .7), tj, pan=.35*np.sin(j*1.9 + t), gain=.12)
    if t >= 5.5:
        for o, mul in ((0, 1), (.75, 1), (1.0, 2), (1.5, 1.5)):
            if not (22.05 <= t + o < 22.9): music.add(bass(hz(ROOT[ch])*mul, .38), t + o, gain=.16)
    t += BAR
tb = 5.5
while tb < 28.0 - 1e-6:
    beat = int(round((tb - T0)/BEAT)) % 4
    if not (22.05 <= tb < 22.9):
        if beat in (0, 2): drums.add(kick(), tb, gain=.34); kicks.append(tb)
        if beat in (1, 3): drums.add(snap(), tb, pan=.08, gain=.22)
        drums.add(shaker(), tb + .25, pan=.35, gain=.4); drums.add(shaker(.5), tb, pan=-.35, gain=.25)
    tb += BEAT
# send press: the hit after the dropout
drums.add(kick(), 22.9, gain=.5); kicks.append(22.9); music.add(thump(55, .5), 22.9, gain=.35)
for i, n in enumerate(['D5','F#5','A5','D6']): music.add(bell(hz(n), 1.4), 22.92 + i*.04, pan=(i-1.5)*.3, gain=.06)
# resolve on the logo, then the same air as the open (loop point)
music.add(pad([hz(n) for n in ['D4','F#4','A4','E5']], 1.6, a=.1, r=1.8, cut=3000), 28.0, gain=.42)
for i, n in enumerate(['A5','D6']): music.add(bell(hz(n), 1.8), 28.02 + i*.08, pan=(i-.5)*.4, gain=.08)

# ---------- sound design (times from relay-film.html) ----------
sfx.add(whoosh(.6, 600, 7000, .2, rev=True), 0.0, pan=.3, gain=.3)   # sphere arrives with its trail
sfx.add(whoosh(.55, 1500, 8000, .6), .55, gain=.14)                  # wordmark slides out from behind the sphere
sfx.add(whoosh(.55, 1500, 8000, .4, rev=True), 2.2, gain=.12)        # retracts
sfx.add(pop(400, 800, .12), 2.9, gain=.3)                            # turns azure
sfx.add(swell(.45, 200, 3000), 3.3, gain=.35); sfx.add(thump(70, .3), 3.72, gain=.3)   # dot floods the frame
for t0 in (3.62, 8.9, 17.98, 18.45): sfx.add(tick(2400, .4), t0)      # chapter titles
sfx.add(whoosh(1.0, 300, 4000, .8), 5.45, gain=.3)                   # tiles converge
for i in range(7): sfx.add(tick(2000 + i*150, .22), 5.9 + i*.07, pan=-.3 + i*.1)
sfx.add(whoosh(.75, 250, 3000, .9), 6.75, gain=.25)                  # push into the column
sfx.add(click(), 8.05, pan=.3, gain=.55)                             # the click
sfx.add(swell(.8, 300, 4000), 8.18, pan=.5, gain=.35)                # bloom floods from bottom-right
# instructions type-on (same accelerating schedule as the film)
INSTR = 'You are a Compliance Agent supporting Legal and Risk teams. You ensure all actions, recommendations, and outputs align with corporate policies, regulatory requirements, and industry standards.'
n = len(INSTR)
def ct(i): return 9.97 + i*.01 if i <= 3 else 10.0 + (i-3)/23*.5 if i <= 26 else 10.5 + (i-26)/124*.5 if i <= 150 else 11.0 + (i-150)/(n-150)*.45
for i, ch in enumerate(INSTR):
    if ch != ' ' and i % 2 == 0: sfx.add(key(.22), ct(i), pan=rng.uniform(-.2, .2))
for t0 in (12.45, 17.5): sfx.add(click(), t0, pan=.5, gain=.5)        # Next / Complete
for t0 in (13.0, 15.0, 16.0): sfx.add(pop(700, 1200, .06), t0, gain=.18)   # card bodies swap
for t0 in (13.3, 13.95, 15.4): sfx.add(tick(3000, .25), t0, pan=.1)  # hover band
sfx.add(whoosh(.7, 300, 3000, .8), 16.2, gain=.25)                   # file stack dragged in
for i in range(3): sfx.add(pop(450 + i*80, 900 + i*120, .08), 17.0 + i*.07, gain=.22)   # files land
sfx.add(whoosh(.5, 200, 3000, .9, rev=True), 18.95, gain=.3)         # card collapses to the icon
sfx.add(pop(500, 1000, .1), 19.4, gain=.3)                           # agent icon
sfx.add(pop(600, 1100, .08), 19.8, gain=.2)                          # input appears
sfx.add(whoosh(.5, 800, 6000, .5), 20.5, gain=.15)                   # expands to composer
sfx.add(pop(380, 700, .1), 21.1, gain=.28)                           # PDF drops in
for i in range(0, 44, 2): sfx.add(key(.2), 21.3 + i/60, pan=0)       # prompt types
sfx.add(riser(.8, 300, 2600), 22.1, gain=.25); sfx.add(whoosh(.8, 300, 8000, .95), 22.1, gain=.35)   # zoom punch
sfx.add(click(), 22.9, gain=.6)                                      # send
sfx.add(whoosh(.35, 300, 5000, .2, rev=True), 23.15, gain=.25)       # zoom back out
sfx.add(pop(420, 820, .1), 23.45, pan=.2, gain=.28)                  # bubble
sfx.add(pop(500, 950, .09), 24.45, pan=-.3, gain=.25)                # agent card
sfx.add(shimmer(1.8), 24.5, pan=-.3, gain=1.0)                       # "Reviewing contract…"
for i, f in enumerate((1175, 1480, 1760)): sfx.add(bell(f, 1.2), 26.55 + i*.06, gain=.07)   # approved
sfx.add(whoosh(.45, 400, 4000, .9, rev=True), 27.55, gain=.2)        # result shrinks away
sfx.add(pop(500, 1100, .12), 28.0, gain=.35)                         # sphere pops
sfx.add(whoosh(.55, 1500, 8000, .6), 28.15, gain=.14)                # wordmark emerges

# ---------- mix ----------
def reverb(b, secs, mixv, seed, damp=7500):
    r = np.random.default_rng(seed); n = int(secs*SR); t = np.arange(n)/SR; out = []
    for ch in (0, 1):
        ir = lp(r.standard_normal(n)*np.exp(-t/(secs*.3)), damp); ir /= np.sqrt((ir**2).sum())
        out.append(fftconvolve(b.L if ch == 0 else b.R, ir)[:N])
    b.L = b.L*(1-mixv) + out[0]*mixv*1.5; b.R = b.R*(1-mixv) + out[1]*mixv*1.5
duck = np.ones(N)
for k in kicks:
    i = int(k*SR); m = min(int(.25*SR), N-i); duck[i:i+m] = np.minimum(duck[i:i+m], 1 - .28*np.exp(-np.arange(m)/SR/.08))
music.L *= duck; music.R *= duck
reverb(music, 2.2, .22, 1); reverb(sfx, .9, .12, 2, 9500); reverb(drums, .6, .07, 3)
L = music.L + drums.L*.9 + sfx.L*.85; R = music.R + drums.R*.9 + sfx.R*.85
L, R = hp(L, 35), hp(R, 35); L, R = L + .45*hp(L, 5000), R + .45*hp(R, 5000)
f = np.ones(N); a = int(29.6*SR); f[a:] = np.linspace(1, 0, N-a)**1.3; L *= f; R *= f
st = np.stack([L, R], 1); st *= .5/np.abs(st).max(); st = np.tanh(st*1.2)/1.2; st *= .85/np.abs(st).max()
wavfile.write('relay-audio.wav', SR, (st*32767).astype(np.int16)); print('ok')
