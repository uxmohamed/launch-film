# Numbers: durations, easing, scale, blur, depth, type (by mode)

## Where these numbers come from
- 59 films were sampled at roughly 2 fps (about 0.5 s per frame). Calibration came from Cosmos (41 frames = 20 s).
- Spacing is **not uniform across films**. Burp's on-screen stopwatch shows about 0.42 s per frame and its playhead about 0.53 s. So treat any duration derived from frames as ±15%.
- Several contact sheets drop duplicate frames. The case files time those films from their original frame indices.
- Cosmos was also studied at its native 25 fps, which gave the precise easing and offsets (see the table at the end).
- Easing at 2 fps is inferred from how the spacing changes: halving gaps mean exponential motion, and shrinking jumps mean ease-out.
- All values assume 1920×1080. Scale them with frame height.

Mode keys: **M1** product/SaaS · **M2** creative tool · **M3** brand/identity · **M4** manifesto/model · **M5** hardware · **M6** documentary.

## Easing families (four, each in its role)
| Role | Curve | Evidence |
|---|---|---|
| Entrances, settles, pull-backs, totals ticking | expo-out `cubic-bezier(.16,1,.3,1)` | At 25 fps, Cosmos words cover ~90% of their travel in the first ~35% of the time. Totals decelerate (9 → 84 → 305 → 737 → 930 → 1009 → 1028). |
| Re-centres, camera travel, pans, card shrinks, width-breathe | ease-in-out `cubic-bezier(.65,0,.35,1)` | Line re-centre, sticky-menu scroll, Netflix width axis. |
| Push-throughs, dot-to-fill, exits, pinches, funnels | ease-in `cubic-bezier(.55,0,1,.45)` or exponential | Flashback halves the window every 0.5 s; zoom-throughs accelerate into blur. |
| UI pops (buttons, chips, pull-to-refresh) | back-out `cubic-bezier(.34,1.56,.64,1)`, 5–10% overshoot | Material's spinner drop, button pops. Never on type or large objects. |

Linear only for constant travel (rail scroll ~120 px/s, orbits, drift), process meters (percentages), real-time tickers and texture.

## The pulse
- The base unit is **0.5 s**, with 0.25 s sub-beats. Almost every film quantises appends, swaps, riffles and cuts to this grid.
- About **2 words/s** is readable when each fragment is 1–3 words (Apple, Wabi, Shapes). Full lines need 1.5–2.5 s.

## Durations
| Element | Range | Notes |
|---|---|---|
| Opening silence / empty ground | 0.5–1.5 s | Or an unreadable macro (M4) |
| Word or word-group append | 0.25–0.6 s (typical 0.4–0.5) | |
| Word entrance settle | 0.35–0.6 s | |
| Late-tail word | +0.3–0.5 s | |
| Full line readable | 1.5–3 s | |
| Word-per-cut captions | 0.5 s per 1–3-word fragment | Wabi, Apple, Coca-Cola |
| Type-only breather | 1.5–3 s | M1 |
| Chapter card | 1–1.5 s | |
| Sibling stagger (readable) | 0.4–0.5 s | Cascades: 1–2 frames. Exits: ~1 frame is fine. |
| Slot-reel swap | 0.45–1 s | 0.5 s for 1–3-word tags once the frame has been read; 0.8–1 s otherwise |
| UI action beat | 1–2 s | |
| Demo step | 1.5–3 s | |
| Reading shot | 2.5–5 s | Big-platform real windows 6–8 s (M1, with a project thread) |
| Longest continuous act | 6–13 s; up to ~30 s in 100 s films | |
| Morph-chain station | 0.4–0.5 s | |
| Push to affordance (3–4×) | 0.8–1.5 s | |
| Zoom-through (10–12×) | ~1 s after a 0.3–0.5 s anticipation | |
| Pull-back macro → context | 0.5 s for 2–3×; 1.5–2 s for 4–5× | |
| Dot/circle fill to ground | 0.2–0.45 s (snap); **~2 s** as a slow glow-bloom climax (Island) | |
| Iris-close on a verb | ~3 s | Index |
| Blur melt | 0.5–1 s | |
| Dither / scanner sweep | 0.6–1 s | |
| Glyph scramble | 0.1–0.3 s per word | |
| Backspace exit | ~2× typing speed | |
| Counter: total | 1–5 s, 3–7 decelerating steps, or 1 jump + a 20% scale-up | |
| Counter: process meter | linear | |
| Riffle / slideshow image | 0.5 s | M2 and M4 run it for 60–80% of the runtime |
| Hidden-subject ladder | holds ×0.8 per shot, 4.5 s → 0.5 s | M4 |
| Black breath | ~2.5 s | M4 |
| Variant flip climax | 2/s for ~2 s | |
| Deliberate hesitation | ~1 s, once | |
| Caret | no blink while typing; 1 s blink cycle when idle | |
| Dim before a chapter change | ~0.5 s at 30–40%, or a 1-frame drop to 50% | |
| Final logo / URL hold | M1 2–5 s · M2 1.5–3 s · M3 1–3 s · M4 2–13 s · M5 1–2 s · M6 2–4 s · short manifestos 1–1.5 s with a bookend | |
| Brand reveal (share of runtime) | M1 long films 15–35%, teasers at the end · M2/M3 0–2 s + end · M4 67–96% · M5 90–95% · M6 35–50% | |
| Film length | teaser 15–30 s · feature 30–60 s · launch 60–110 s | |

## Scale and camera
| Move | Range |
|---|---|
| Hold drift | ±3–5% over 2–3 s (it can shrink ~15% to anticipate multiplication); float ±5–10 px |
| Logo / title push | ~1.1× |
| Feature detail push | 1.4× |
| Push to affordance | 3–4× (the send button ~3.5×) |
| Dive into a component | 3–6× |
| Key-click macro punch | 6–8×; Spellbook's typed redline 15× |
| Zoom-through | 10–12× |
| Macro working crop | 2–4× |
| Pull-back payoff | 2–5× |
| Word truck | text at 40–60% of frame height, wider than the frame; 6× + 10° tilt for a title sweep |
| Oversize-settle | 150–160% (type) up to 1.75–2.5× (logomarks) → 100% |
| Undersize-rise | ~60% → 100% |
| Image entrance pop | 0.55 → 1.0 |
| Kick-synced pulse | +2–3%, τ ≈ 0.14 s |
| Press feedback | 95% → 100%; sibling-coupled: pressed +20% width, siblings shrink |
| Full window | 70–80% of frame width |
| Floating card | 25–45% of frame width; giant prompt pill ~60% |
| Scene → card target | 45–50% of frame width |
| Row that keeps its width | total held at ~60% of frame width as tiles are added |
| Shrinking-history funnel | each step 25–40% smaller |
| Scale-descending reel | each item ~50% of the previous |

## Blur
| Use | px at 1920 |
|---|---|
| Word / pill arrival | 8–12 → 0 over ~0.5 s (Cosmos 25 fps: 9 → 0) |
| Caption value blur-in | ~4 → 0 over ~2 frames |
| Blur-scatter exit | 0 → ~10 |
| DOF, back plane / non-selected | 4–10 |
| Near plane | 8–12 |
| Frosted glass HUD | backdrop 20–30 + a 1 px white stroke |
| Blur-the-world reaction | ~30 + darken, with one element sharp |
| Blur-bloom "generate" | ~40, then a focus pull (~1 s) |
| Scene melt | 60–80 over 0.5–1 s |
| Photo → gradient ground | 0 → 80 at 3× |
| Background blobs | ~20% of frame width (300–400) |
| Glow-cool arrival | 15–25 glow → 0 |
| End blur-out | 0 → 15 + fade over 1.5 s |
| Zoom-through | directional, + 1–2% RGB offset |

## Opacity and luminance
- Ghost word 25–40%. Slot-reel neighbours 25–40%. Inactive menu items ~20%. Status-log history ~40%.
- Dimmed context ~50%. Data around a spotlight 12–25%. The echo word behind a status ~8% contrast.
- Card shadow: blur 20–30 px, 5–6% opacity, y 6–10 px. Outline motifs on colour: 1 px at ~20%.
- Overlay washes on footage 60–80%. Rim-lit hardware body ~5% luminance.

## Type size by mode (cap height or font size as % of frame height)
| Mode | Body / statement | Emphasis |
|---|---|---|
| M1 product | 1.2–3.5% (social-first 7–10%) | one shout at 25–40%, or a whisper inversion |
| M2 creative | mixed, many faces | output-set words; 10+ shouts are acceptable when range is the claim |
| M3 brand | 7–15% | super-shouts at 35–60%, words wider than the frame, size alternation |
| M4 manifesto | 1.2–5% | whisper peak, diegetic words, annotation |
| M5 hardware | 6% corner caps | undersize-rise, random-letter fill |
| M6 documentary | 4–5% captions; 12–15% behind the speaker | stats at 8–15% |
| UI text rebuilt for film | 3–5% | |
| End logo | M1/M4 4–5% · M3 25–45% · others 5–12% | |

- **Families:** one grotesk + mono by default. A second voice is allowed with a fixed role: an italic serif for the "human" or emphasis word (Copilot, Arena, Island), or a literary serif as narrator with the grotesk for the product (Spellbook).
- **Tracking:** −1 to −2% on headlines. Word gap ~0.28 em. Pill padding ~0.4 em, pill height 1.4× the font size, radius ~0.4× the pill height.
- **Rise offset:** ~0.8× the font size (Cosmos: 38 px at 46 px type, ~0.45 s). Subtle variant: 3–5 px.
- **Typing speed:** 6–8 characters per 0.5 s (readable), ~15 characters per 0.5 s (hero prompt, Lovable ≈ 30 characters/s), 40–60 characters per 0.5 s (texture).

## Colour
- One ground + neutrals + one accent **with meaning**. Allowed extensions:
  - two accents with fixed meanings (Cowork: salmon = task, blue = selection; t0: green = right, pink = wrong);
  - strict duotone pairs per chapter (M3);
  - grounds taken from the artwork (M2);
  - a transient hue-cycle that settles to the one accent (ChatGPT).
- Grounds can encode act, argument, rhetoric or presence (see SKILL §2.5).
- Emphasis polarity: on light grounds, dark emphasis; on dark grounds, white (the only solid bar).

## Calibration: Cosmos (20 s, native 25 fps)
| t (s) | Event |
|---|---|
| 0.08 / 0.24 / 0.56 / 0.72 | Words 1–4 enter (rise ~0.8 em, expo-out ~0.5 s) |
| 1.50 | The pill slides in from ~+70 px; its text rises and blurs in from +0.14 s |
| 1.84 | "?" arrives |
| 2.06–2.46 | Earlier words fade out L→R (0.07 s stagger); the line re-centres on the pill (0.6 s ease-in-out); "?" fades |
| 3.28 | Hard cut on the downbeat to the interleaved row: the hero image + 2 labels |
| 3.36 / 3.42 / 3.64 / 4.00 | Labels, neighbour images, outer labels and outer images join (the row grows symmetrically) |
| 5.34–5.62 | Labels drop and fade; the hero grows 1.0 → 1.22 |
| 5.64 | Cut to the detail card; it settles 0.55 s (expo-out) while panning to its lower half |
| 5.72–6.36 | Caption pieces arrive (text → pill → text; line 2 at +0.56 s) |
| 7.56 / 8.12 / 8.36 / 8.76 | Hard-cut slideshow with captions already in place |
| 9.04 / 9.20 / 9.36 | Three buttons pop (back-out, rising 34 px) |
| 9.46–10.08 | Crossfade into the phone; scale 1.9 → 0.94 (expo-out) |
| 10.64–10.94 | Re-zoom to 1.3× on the lower screen (ease-in-out) |
| 11.1–12.1 | The tap dot travels, presses and releases |
| 12.12–12.40 | Dim → new screen; the camera eases out to reveal the top |
| 12.64–12.86 | Search types |
| 12.96 / 13.08 / 13.20 | Grid rows stagger in |
| 13.5–15.25 | The grid scroll accelerates then decelerates; the phone shrinks to 0.8 |
| 15.30 | Cut to empty ground |
| 15.32 / 15.48 / 15.60 / 15.96 | "Now" / "live" / "on" / pill |
| 17.76 | Cut to the logo: letters rise with a 45 ms stagger, then ® |
| 17.76–20.0 | Hold |
