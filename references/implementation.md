# Implementation: building and rendering the film

This is a proven pipeline: a single HTML file with a deterministic `render(t)` function, frame-accurate capture in headless Chromium, and ffmpeg for the encode. A working 20 s example is in `examples/cadie-film.html` and `examples/render.js`. Read it before building.

## Architecture
1. **Stage.** A 1920×1080 `#stage` div, scaled to fit the viewport with a CSS transform. At capture time the scale is 1.
2. **Deterministic timeline.** One function `render(t)` sets *every* element's transform, opacity and filter from `t` alone. It has no CSS transitions, no `setTimeout` and no animation state. This makes scrubbing, reversing and frame capture exact.
3. **Helpers** (copy them from the example):
   - `bezier(x1,y1,x2,y2)`: a cubic-bezier solver. Define `EO`, `EIO`, `EI` and `BACK` from `numbers.md`.
   - `P(t, t0, dur, ease)`: eased progress from 0 to 1, clamped.
   - `tf(el, x, y, scale, opacity)`: sets a `translate3d` + scale transform and opacity.
   - `Line(parent, items, opts)`: a word-append line with live re-centring. Each item has `tin` and `tout`, and its layout width factor eases 0→1 with expo-out, so the line re-centres on its own as words arrive and leave. Pills get a slide-in box plus text that rises and blurs in.
4. **Scenes.** Each scene is a container. Toggle it with `display`, **not** `visibility`: a child set to `visibility:visible` shows through a hidden parent. Visual continuity between scenes is done inside `render` by aligning transforms (for example, the outgoing scene scales with the incoming phone camera).
5. **Camera.** Model the camera as keyframes returning `[scale, cx, cy]` per time range (see `phoneCam` in the example), each segment eased. Apply the camera to a world container, not to each element.
6. **Assets.** Prefer real product UI rebuilt in HTML/CSS at film type sizes. For imagery, use real brand photography. If none exists, procedural canvas painting plus a gradient map to the brand palette plus grain works as a placeholder (see `paint*` in the example), but real photography will always look better.
7. **Fonts.** Load them via Google Fonts or local `@font-face`, and wait for `document.fonts.ready` before measuring text widths. Line layout depends on measured widths.

## Capture and encode
```bash
npm i playwright-core   # in a scratch dir; uses a cached Chromium (see render.js)
CHROME=<path-to-chrome-headless-shell> PW=<path>/node_modules/playwright-core node render.js 30        # full film → cadie.mp4
CHROME=... PW=... node render.js 30 1.8 3.5 5.8 9.4 12.8 18.5                                          # stills at chosen times
```
- The page exposes `window.renderAt(t)`, which renders and then waits two animation frames. `?capture` hides the UI chrome.
- Frames are piped as JPEG (q95) into `ffmpeg -f image2pipe` with libx264 at crf 16, yuv420p and faststart, muxed with the audio WAV.
- A 20 s film at 30 fps takes about 65 s to render on an M-series Mac.

## Review loop (do this every iteration)
1. Render stills at **every scene boundary (±1 frame)** and at every beat's midpoint.
2. Tile them into a contact sheet (PIL, 4–5 columns, with timestamps) and look at them.
3. For the finished film, build a side-by-side sheet against the reference:
   ```bash
   ffmpeg -i ref.mp4 -i out.mp4 -filter_complex "[0:v]fps=2,scale=480:-1[a];[1:v]fps=2,scale=480:-1[b];[a][b]hstack,tile=4x10" -frames:v 1 sbs.png
   ```
4. To study a new reference video, extract it at 5 fps with a timestamp overlay, tile 20 frames per sheet, then do a frame-by-frame strip (native fps) on each transition. Run a scene-cut check with `select='gt(scene,0.2)'`.

## Reading a reference library from Figma
Frame-grid sections, where each frame is a 480×270 thumbnail:
- Get the section list and the frame coordinates with `get_metadata`. It returns a large result; parse it as XML with Python.
- Get each section at full resolution with `get_screenshot` (`maxDimension` = the section height), then slice it locally with `examples/contact_sheet_slicer.py` (20 frames per sheet, labelled `#n`).
- **Rate limits:** Starter plans allow 20 MCP calls per month, Pro allows 200 per day at 10/min, and Enterprise Full seats allow 600 per day at 20/min. The file must be in a team where the connected account has **edit** access.
- If one Figma MCP connection returns "you don't have edit access" even though the file is shared, try any other configured Figma connection before asking the user to change sharing. One can fail while another succeeds. Run `whoami` to see which account and seats a connection uses.
- A section whose width is greater than its height gets clamped if you set `maxDimension` to its height. Pass `max(width, height)`.
- Farm the per-film analysis out to parallel agents with a shared brief (see the `_brief.md` pattern: shot list, transition inventory, easy-to-miss details, pacing, reusable techniques, cross-film patterns).

## Common bugs
- **Scenes bleeding into each other:** you toggled `visibility` instead of `display`.
- **Captions stacking:** the same cause, in per-item groups.
- **The row overflows the frame:** compute the total width and scale the row to at most ~85% of the frame width.
- **Text measured before fonts load:** layout jumps. Await `document.fonts.load(...)` for every weight you use.
- **Blob URLs used before decode:** `await img.decode()` on each one before the first render.
