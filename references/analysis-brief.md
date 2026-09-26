# Analysis brief: studying a new reference film

Use this brief when you add films to `cases/`. Give it to each analyst (a person or an agent), together with the film's contact sheets.

## Input
- Sample the film to sequential frames at ~2 fps (≈0.5 s apart). Calibrate against a known runtime, and treat durations as ±15%.
- Tile 20 frames per sheet, 5 per row, each labelled `#n` in playback order. `examples/contact_sheet_slicer.py` does this from a frame grid.
- For precise easing, also study one transition at the film's native fps.

## Read everything
Open every sheet in order. The in-between frames are where the craft lives.

## Write `cases/<Film>.md`
1. **One-line concept:** what the product is, and the narrative spine of the film.
2. **Visual world:**
   - background and palette;
   - type (family, weight, size as a percentage of frame height);
   - imagery style;
   - how the UI is staged (flat card, device, macro crop, redrawn...);
   - depth, and recurring motifs.
3. **Shot list:** a table of frame range, estimated duration, shot type, what's on screen, camera, element motion, and how it exits into the next shot. Be literal about what changes between adjacent frames.
4. **Transition inventory:** every transition, with its mechanism and what motivates it.
5. **Easy-to-miss details:**
   - drift during holds;
   - delayed secondary motion, staggers, overshoot, motion blur;
   - masked reveals, parallax;
   - cursor behaviour, how emphasis is made, how text is revealed, counters.

   Estimate magnitudes (scale %, blur px at 1920, offsets, durations).
6. **Pacing curve:** where the film is slow or fast, where it breathes, the climax, and how the ending lands.
7. **What makes it premium:** concrete, not generic.
8. **Reusable techniques:** 3–8 named patterns, each with a recipe (structure, timing, easing).

## Then compare against the manual
End a batch with a crosscut file:
- patterns that recur across the batch;
- contradictions between films, and why they happen;
- numbers you can infer.

Finish with **"vs. the manual"**:
- (a) techniques that aren't in `SKILL.md` or `taxonomy.md` yet;
- (b) places where the films contradict its rules or numbers;
- (c) rules the films strongly confirm.

## Rules
- Cite frame numbers.
- No generic motion advice. "Use easing" is worthless.
- Don't describe music.
- Brand films aren't SaaS demos: analyse them for their motion system, not for UI staging.
