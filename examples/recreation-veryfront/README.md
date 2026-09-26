# Recreation: the Veryfront case

A complete, shot-by-shot recreation of [`references/cases/Veryfront.md`](../../references/cases/Veryfront.md), a 30-second launch film for an AI-agent builder. It's a finished reference film you can study, scrub and reuse instead of starting from zero.

The brand is replaced with a fictional one, **Relay**, and so are the third-party integrations and model names. The motion design, timing and structure follow the case's frame-by-frame breakdown. The recreation was checked by rendering stills at all 61 of the case's frame times and comparing them side by side with the original.

- `relay-film.html`: the film. Open it in a browser; press Space to play, or drag the scrubber.
- `relay-film.mp4`: the rendered film (1920×1080, 30 fps) with score and sound design, mastered to -14 LUFS.
- `make_audio.py`: generates `relay-audio.wav` (Python 3 with `numpy` and `scipy`). The score runs at 120 BPM, so one beat is the film's 0.5 s pulse. It drops out under the zoom punch and hits on the send press. Every sound effect sits on its frame event.
- `render.js`: re-render it. `CHROME=<chromium path> node render.js` writes the MP4, adding `relay-audio.wav` if you've run `make_audio.py` first; `node render.js 30 4 8.5 23` writes review stills.

## Shot map

Each block in `relay-film.html` is labelled with these frame ranges (~0.5 s per frame).

| Case frames | Time | Shot | Technique (see `references/taxonomy.md`) |
|---|---|---|---|
| #1–5 | 0–2.5 s | Sphere arrives with a trail; the wordmark slides out from behind it | **Logo-as-mask wordmark**: the mask edge is the sphere's circumference; the lock-up re-centres live |
| #6–8 | 2.5–4 s | Wordmark retracts; sphere turns flat azure and grows | **Brand dot → circle reveal**: the brand colour comes out of the logo |
| #9–11 | 4–5.5 s | "Choose Agent" on blue, with rotating outline ellipses | Chapter coding by ground; the motif rotates ~9°/s |
| #12–15 | 5.5–7.5 s | Scattered agent tiles converge into a column | **Chaos → order**: 3 depth planes, back and front blurred |
| #16–18 | 7.5–9 s | Macro on "Compliance Agent"; the cursor clicks; blue floods in | **Depth-of-field selection**, the **hero cursor**, and a **click-direction bloom** from the cursor's entry side |
| #19–20 | 9–10 s | "Customize Agent" with concentric circles | Per-chapter variant of the same motif |
| #21–26 | 10–13 s | "Add Instructions": accelerating type-on | **Hot text**: newest characters pink → blue → cool to grey; Next fills with the brand gradient on press |
| #27–32 | 13–16 s | Integrations, then models | **Wizard body swaps** in one persistent card; the hover band trails the cursor by a frame |
| #33–36 | 16–18 s | Files dragged in as a fanned stack | Object carried by the cursor; "Next" relabels to "Complete" |
| #37–39 | 18–19.5 s | "Your agent is ready" (the full line is reserved, words append) | Chapter card |
| #39–42 | 19–21 s | The blue card collapses (octagon corners) into the agent icon; input appears | **Chapter card → icon collapse** |
| #43–45 | 21–22.5 s | The input expands into a composer; PDF dropped; prompt types | Container morph + hot text |
| #46–47 | 22.5–23.5 s | Extreme zoom on the send button; it turns blue on press | **8× zoom punch**: the cursor scales with the camera |
| #48–53 | 23.5–26.5 s | Dark bubble drifts up-right; agent card "Reviewing contract…" | **Shimmer** instead of a spinner |
| #54–56 | 26.5–28 s | "Contract approved" result | Blur-in with the late text; shrink to nothing |
| #57–61 | 28–30.5 s | Sphere pops; wordmark emerges; hold | **Palindrome**: the film ends exactly as it began, so it loops |

## Implementation notes

- Everything is driven by one deterministic `render(t)`. There are no CSS transitions, so every frame is exact and scrubbable.
- Four easing roles only: expo-out entrances, ease-in-out camera and re-centring, ease-in push-throughs and fills, and back-out for pops.
- Each cursor instance gets unique SVG gradient ids. A shared id inside a hidden scene makes Chrome drop the fill.
- Camera moves use `cam(container, scale, focusX, focusY, screenX, screenY)`. Interpolate the screen point too, so scale 1 is the identity.
