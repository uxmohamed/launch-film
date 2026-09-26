# Figma Draw (feature launch) — 52 frames ≈ 26 s

## 1. One-line concept
A launch for Figma's illustration toolset (brushes, text on path, progressive blur, vector editing, texture). It has no sentence at all. The spine is a riffle of **finished artworks**, each shown at the moment one tool is applied. It opens on a title card whose word "Draw" is redrawn by each brush, and ends by pulling back from the last artwork into a real website layout.

## 2. Visual world
- **Ground:** each artwork is its own world, a full-bleed, saturated poster colour field:
  - sage green (#7–9);
  - tan (#10–13);
  - pastel poster grid (#14–15);
  - salmon pink (#16–22);
  - a photo of a tiled wall (#23–30);
  - lime (#31–40);
  - a green-lavender gradient (#41–48);
  - brown (#49–52).

  It opens on black.
- **Type:** the title is Figma's grotesk, white, at about 7% h. Art typography varies: rounded marker lettering, condensed orange caps (CHESAPEAKE), geometric orange "VOLUME", a heavy lime "NATURE FEST".
- **UI:** real Figma Draw chrome, but only as floating fragments: the bottom toolbar (#7–9), the Brushes panel (#10–13), the Layer blur panel (#25–30), the Texture panel (#41–45). The panels are small (about 12–15% of frame width) and sit over the art with a soft shadow. Vector handles, selection boxes and paths are drawn at artwork scale in Figma's blue.
- **Imagery:** illustrative, with halftone, grain, noise textures and gradient meshes. It is deliberately not "UI design" content, so the audience reads Figma as an illustration tool.

## 3. Shot list
| Frames | ~s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1 | 0.5 | Black | – | – | – | title |
| #2–6 | 2.5 | Title, variant flips | "Figma Draw". Each frame, "Draw" (and an underline scribble) is re-rendered in a new brush: a lime scribble under "Figma" (#2), a red pencil hatch plus a scribble (#3), a lavender→orange gradient (#4), yellow marker plus an underline (#5), a pink→green gradient (#6). The title slides left about 3% by #6 | slow drift | style slot reel at 2/s | cut |
| #7 | 0.5 | UI fragment | the toolbar alone on sage green; the pen/brush/pencil tools stand raised | locked | – | strokes draw around it |
| #8–9 | 1 | Draw-around | black brush strokes draw a doodle face and a tail **around the toolbar**, which stays put | locked | strokes draw on | cut |
| #10–13 | 2 | Macro art + panel | a mouse character with a halftone sweater and scribbled letters; the Brushes panel at right; the cursor picks a brush and the "U" strokes change texture | slight push | the cursor hovers down the list; the selected row highlights | cut to grid |
| #14–15 | 1 | Variant grid | about 9 "Sunday skate club" posters in different colourways, cropped at the frame edges | slow pan right | the cursor clicks one | cut |
| #16–18 | 1.5 | Text on path | blue Bézier curves with orange "CHESAPEAKE" text flowing along them | the camera rides the curve (moves up and right) | the text slides along the path and a handle moves | cut |
| #19–22 | 2 | Badge | a circular text badge on an ellipse path, on pink with black leaf silhouettes | locked | the text **rotates around the ellipse** about 30° per frame; the path handle is visible at #19 | cut |
| #23–30 | 4 | Progressive blur | "VOLU(ME)" orange caps over a tiled-wall photo; the cursor draws a vertical blur axis, the Layer blur panel opens (Progressive), and the End slider drags 0 → ~40 | slow truck left about 10% | the blur increases on the right part of the photo and the type | cut |
| #31–35 | 2.5 | Vector edit | a black butterfly on lime; a hatched selection on the right wing, then its path is reshaped into a curl | locked | points drag and the shape rebuilds live | cut |
| #36–40 | 2.5 | Macro vector | a gradient butterfly with handles; a dashed wedge (rotation sweep) → a rotated bounding box → the background gradient fades in | slight push | the handles stay visible | cut |
| #41–45 | 2.5 | Texture | a macro bird-shape with the Texture panel (Size, Spread); the Spread slider drags up and noise grain spreads across the shape | locked | a real-time grain increase | pull back |
| #46–48 | 1.5 | Reveal | pull back to a symmetric butterfly over "NATURE FEST" lettering | zoom out about 2.5× | – | continues out |
| #49–52 | 2 | In context | the poster sits in a website layout (Events section) on a brown ground | continued zoom out about 1.5× | – | end (no logo) |

## 4. Transition inventory
- **Style-variant flips on the title** (#2–6): the same word is redrawn in a new brush every 0.5 s. Here the variant flip is applied to the brand title itself.
- **Draw-around-UI** (#7→9): the toolbar is the anchor, and the art is drawn around it. The UI is the cause of the art.
- **Hard cuts between artworks:** all other boundaries are hard cuts. Continuity comes from the cursor and the Figma-blue handles, not from any object.
- **Pull-back into context** (#45→52): a continuous zoom out, from grain macro → the full poster → the poster in a website. This is the only camera move longer than 1 s.

## 5. Easy-to-miss details
- In the title, the underline scribble belongs to a different word each time (under "Figma" at #2, under "Draw" at #3 and #5), as if the brush were testing itself.
- The toolbar's raised pen tools (#7) are the product's own "selected tool" state, reused as a hero pose.
- The Brushes panel cursor goes **down** the list over 3 frames (#11–13), and the letter texture swaps each time.
- In #19–22 the badge text rotates while the leaves stay still, which separates the verb (text on path) from the art.
- The progressive-blur truck (#23–30) moves the photo left while the panel stays screen-fixed, so the UI reads as a HUD over a moving world.
- The Spread value visibly jumps through 4 → 60 → 85 (#41–45) while the grain grows. The numbers change with the effect.
- There is no end logo. The final frame is the artwork in a website: "Draw ships work."

## 6. Pacing curve
- It is even throughout: 1–2.5 s per tool and about 8 tools in 26 s.
- It opens with a 2.5 s title flip, and the fastest passage is the brush flips at 2/s.
- The longest single take is the progressive blur (4 s), the most "invisible" feature, so it gets the most time.
- It ends on a 3.5 s pull-back rather than a card: an arrival, not a subtraction.

## 7. What makes it premium
- Every example is a finished, art-directed piece, never a demo scribble.
- The UI appears only as the cause, at small scale, and floats over full-bleed art.
- The ground colour changes with every artwork, yet the Figma-blue handles unify the film.
- The feature is shown mid-action (slider mid-drag, grain mid-growth), never as a before/after.

## 8. Reusable techniques
1. **Self-restyling title.** Re-render the product name (or one word of it) in a new tool style every 0.5 s for 5 frames, with a slow 3% drift. It works best when the product *is* a style tool.
2. **Draw-around anchor.** The UI element sits still at the centre while the result draws itself around it over 1 s.
3. **Panel-over-art.** Show a real settings panel at 12–15% of frame width over a full-bleed artwork, with the cursor dragging one slider through 3–4 visible values while the art changes live. 2.5–4 s.
4. **World-moves, HUD-stays.** Truck the artwork about 10% while the panel stays pinned to the screen.
5. **Macro → artwork → context pull-back.** Three nested scales (grain → poster → website) in one continuous zoom-out of about 4× total over 3–4 s, instead of an end card.
