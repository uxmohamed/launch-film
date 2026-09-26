# Uber Icon System (Base), analysis (82 frames, ≈41 s)

*This is a brand and design-system film. Read it for the motion system: how a set of adjectives becomes kinetic type, and how icons behave as letters.*

## 1. One-line concept
The launch of Uber's new icon system in its Base design system. The spine is a **list of adjectives, each typeset to perform itself**: "Introducing / A new icon system / From — Base" → OPEN (outlined on a construction grid) → LIGHTER (the weight thins) → FRIENDLIER (the baseline bends into a smile) → icon principles (2 px stroke, geometrical, open negative space, smoothly curved) → icons become letters (A C V D) → "Designed to work seamlessly with our typeface Uber Move" → a paragraph with icons as words → ACCESSIBLE → the nav-bar demo → SCALABLE → "Over 1,500 unique icons" → icon wall → MORE FUNCTIONAL / ACROSS PRODUCTS → app-icon carousel → "One Uber" → "One" → Base logo. **Each adjective is a verb for the type.**

## 2. Visual world
- **Ground:** binary. Pure black #000 for statements (#1–#17, #33–#37, #43–#45, #53–#58, #63–#66, #74–#82) and pure white for specimens (#18–#32, #38–#42, #59–#62, #67–#73). The switch between them is a hard cut and acts as a chapter break. No gradient, texture or grid, except the construction grid in #11–#12.
- **Type:** Uber Move (a geometric grotesk), uppercase for the adjectives, cap height ~8–10% of the frame; sentence case for body (~3–4%). The word **is** the illustration: OPEN is set as outline with a keyline grid, LIGHTER in a hairline weight, FRIENDLIER curved on a Bézier.
- **Icons:** black 2 px line icons with a single **light-blue accent stroke segment** (#19–#26: the blue bar under the warning triangle, the blue arc on the refresh icon, the blue fill in the pin). The accent is used to annotate the principle being named, then removed (#27 all black).
- **Staging:** icons sit on white tiles with a very faint shadow (~2% opacity) (#18–#26). App demo: a cropped phone bottom (tab bar, food photos), frameless on black (#45–#52). App icons are big squircles in a carousel (#68–#73).
- **Colour:** B&W + one light blue (annotation) + the Uber Eats green (only on the app icons, #69–#71).

## 3. Shot list
| Frames | ≈s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1 | 0.5 | Black | empty | — | — | fade |
| #2–#3 | 1 | Type | "INTRODUCING": grey (#2, ~60%) → white (#3) and slightly **larger** (~105%) | locked | fade-up + scale-up | cut |
| #4–#7 | 2 | Type | "A NEW" → "A NEW / ICON SYSTEM" (left-aligned, 2 lines) → a gap opens between ICON and SYSTEM (#6) and an icon **cycles** in it: music notes (#6) → road (#7) | the block **shifts left** as it grows (#5 → #6) | inline icon slot: an icon every 0.5 s | cut |
| #8–#10 | 1.5 | Type | "From ——— Base": a long hairline rule between the words (#8, the words at the frame edges) **retracts** to a short dash (#9–#10) as the words slide together | locked | line length 60% → 5% of the frame in 0.5 s (ease-out) | cut |
| #11–#12 | 1 | OPEN | "OPEN" as a 1 px outline over a construction grid with bounding-box handles at the corners | slow push ~3% | the grid lines hold still, the word drifts | cut |
| #13–#14 | 1 | LIGHTER | "LIGHTER" extra-bold (#13) → hairline and **wider** (#14) | locked | a weight-axis animation from black to thin; the word gets wider | cut |
| #15–#17 | 1.5 | FRIENDLIER | a white Bézier curve with diamond handles enters from the top corners as a V (#15, "FRIENDLIER" grey, curved) → the curve relaxes into a U/smile (#16–#17); the word, set on the path, whitens | locked | the path's control points move and the text follows the path | cut to white |
| #18 | 0.5 | Icon | a bold filled "eye/warning" triangle on a white tile | locked | — | morph |
| #19–#21 | 1.5 | Principle | the triangle → a line **warning icon** with a blue accent under it; caption "2 px stroke" (#19); a second tile, refresh, slides in right with "Geometrical" (#20–#21) | the row re-centres as tiles are added | the blue accent segment marks the principle | tile added |
| #22–#26 | 2.5 | Principles row | a pin tile with the caption "Open negative space" (#22 grey → #23 black, a caption fade-in); a bubble tile "Smoothly curved" (#25); the row **shrinks** each time a tile joins (#21 2 tiles large → #26 4 tiles small) | the row re-centres | the blue accent moves to whichever part of the icon illustrates the principle | tiles dissolve |
| #27 | 0.5 | Icons bare | the tiles and captions vanish; the 4 icons in black, all accents gone, sitting on a thin grey **baseline** | locked | — | icons → letters |
| #28–#29 | 1 | Icons as letters | the icons **morph into letters** on the same baseline: warning → A, refresh → C (#28 is a half-morph "◡", #29 C), pin → V, bubble → D | locked | a per-glyph morph over ~2 frames | type |
| #30–#32 | 1.5 | Typing | "Desi|" → "Designed|" with a caret on the baseline (large, ~12% cap); then an icon (sliders) appears after the word as though typed (#32) | locked, then #32 slight pan left | typewriter; the icon is typed like a character | shrink to black |
| #33–#37 | 2.5 | Sentence | on black: "Designed ⚙ to work ◎ seamlessly / with our ⚡ typeface 💬 Uber 🚗 Move": the second line is typed with **selection boxes and coloured cursors** (blue, orange, green) moving over words, like multiplayer Figma (#34–#36) | locked | each word gets a coloured bounding box as it is placed; the cursor labels leave on #37 | cut to white |
| #38–#42 | 2.5 | Paragraph | "We ◎ reimagine" large (#39), then a **pull back** to a full paragraph (#40–#42) where every few words there is an inline icon ("We reimagine the way the 🌐 world moves for the better. Movement 🚗 is what we power…") | pull back ~2.5× then slow scroll up | the paragraph types in (the bottom line is still arriving, #41 lighter) | cut |
| #43–#45 | 1.5 | ACCESSIBLE | "ACCESSIB|" with the letters **brightening left to right** (#43, the right is darker, like a contrast ramp) → full white (#44) → the word **drops down** as a phone tab bar slides in from the top (#45) | locked | contrast sweep; push-down by the incoming UI | UI enters |
| #46–#52 | 3.5 | Nav demo | a cropped phone: food photos + tab bar (Home / Grocery / Explore / Orders / Account); the **selected tab walks** left to right, one per frame: Home filled (#46–#47) → Grocery (#48) → Explore (#49) → Orders (#50) → Account (#51); #52 zooms in ~1.3× | slow push | each selected icon switches from outline to **filled** | cut |
| #53–#55 | 1.5 | SCALABLE | "SCALABLE" solid in the middle, with 4 outline echoes stacked above and below (#53–#54), then **wipes off left** (#55 a sliver at the left edge) | slight push | the echoes shift vertically, like a repeat/step-and-repeat | wipe |
| #56–#58 | 1.5 | Number | "OVER 1,500 UNIQUE ICONS": the digits **roll like a slot machine** (#56 "0,04…" mid-roll, #57 "1,4?0", #58 "1,500") | locked | per-digit vertical roll with digits cut by the line mask | cut to white |
| #59–#62 | 2 | Icon wall | 6 icons on white (#59) → a grid of ~50 (#60) → hundreds (#61) → the wall **tilts/warps** (#62, a rotated, perspective-bent field) | pull back fast (≈×2 per frame) | the grid densifies as the camera retreats; the last frame bends as if on a sphere | cut |
| #63 | 0.5 | Type | "MORE / FUNCTIONAL" | locked | — | cut |
| #64–#65 | 1 | Type | "ACROSS" → "ACROSS / PRODUCTS" | locked | append | wordmark |
| #66–#67 | 1 | Wordmark | a huge "Uber" white on black (#66, fills ~60% of the width) → a **white irregular polygon wipe** cuts in from the corners (#67), turning the black into a hexagonal badge | locked | the mask shrinks the black to a shape | shape → icon |
| #68 | 0.5 | App icon | the black shape settles into the Uber app-icon squircle on white | locked | contraction | carousel |
| #69–#73 | 2.5 | Carousel | the app icons slide left one per frame: Uber Eats (green), Uber Driver, Uber Orders, Uber Merchant (Postmates courier), Uber Freight; the centre icon is large and saturated; the neighbours are small and grey; the label below changes | horizontal pan ~1 icon per 0.5 s | the centre-focus scale ~1.3× and desaturated neighbours | cut to black |
| #74–#75 | 1 | Type | "One Uber" grey (#74) → white (#75) | locked | fade-up | subtract |
| #76–#77 | 1 | Type | "Uber" drops out and "One" re-centres | locked | subtraction | morph |
| #78–#82 | 2.5 | Logo | "One" becomes the **Base logomark** (a rounded diamond with a play triangle), which then sits beside "Base" | locked | the mark appears alone (#78), then the wordmark appends (#79); holds 1.5 s | end |

## 4. Transition inventory
- **Adjective as typographic behaviour** (#11, #13→#14, #15→#17, #43, #53): each word is animated by the property it names: OPEN outlined, LIGHTER losing weight, FRIENDLIER bending into a smile, ACCESSIBLE rising in contrast, SCALABLE in step-and-repeat.
- **Rule retract** (#8→#10): a line between two words shrinks to a dash, pulling the words together.
- **Inline icon slot** (#6→#7): a gap in the headline cycles icons.
- **Icon → glyph morph** (#27→#29): four icons become the letters A C V D on a shared baseline. The best single moment: it proves "designed to work with our typeface" without saying it.
- **Caret-typed icon** (#31→#32): an icon typed like a character.
- **Multiplayer selection** (#34→#36): coloured cursors and bounding boxes place words, a design-tool vernacular.
- **Pull back to paragraph** (#39→#40).
- **Word pushed down by UI** (#44→#45): the tab bar descends and displaces the word.
- **Selected-state walk** (#46→#51): the selected tab steps across the bar once per frame, a cut-free slideshow.
- **Echo wipe** (#54→#55).
- **Slot-machine digits** (#56→#58).
- **Density pull-back** (#59→#62): 6 → 50 → hundreds, then a perspective bend.
- **Wordmark mask-to-badge** (#66→#68): the black ground around the white "Uber" is cut by a polygon wipe into the app-icon shape.
- **Carousel pan** (#69→#73).
- **Subtraction to logo** (#75→#78): "One Uber" → "One" → the Base mark.

## 5. Easy-to-miss details
- "INTRODUCING" does a **grey→white with ~5% scale-up** in 0.5 s (#2→#3). Many of the word entrances use grey-then-white, e.g. "One Uber" #74→#75 and "Open negative space" #22→#23. The arrival state is **grey**.
- In the principles row, the tile row **scales down as each tile is added** so the whole row stays at ~60% of the frame width (#21 → #26).
- The blue accent is **explanatory**: under the triangle's base for "2 px stroke", on the arc's end for "geometrical", filling the pin's head for "negative space". It vanishes when the icons become letters (#27).
- The half-morph refresh → C (#28 "◡") is visible for exactly one frame: the arc rotates and loses its arrowhead.
- The multiplayer cursors are **three colours** (blue, orange, green) with name-tag flags (#35 shows one at the right edge, "Uber"), echoing Figma collaboration.
- In ACCESSIBLE (#43) the letters on the right are dim and the left ones bright: a left-to-right contrast ramp that suggests legibility being turned up.
- In the tab-bar walk, only one icon is filled at a time and the photos above never move. Only the variable changes.
- The digit roll (#56) uses **clipped digits** (the tops and bottoms of the next/previous digits are visible, cut by a line mask), like the manual's slot reel applied to numerals.
- The icon wall's last frame (#62) is **warped**, a spherised field, as though the camera flew too far back.
- The final Base mark carries a **play triangle**, a nod to motion.

## 6. Pacing curve
The film is very regular. It is a drumbeat of ~1–1.5 s statements, alternating with 2–3.5 s specimens (principles row, sentence, paragraph, nav demo, carousel). Every statement is a hard cut on black, every specimen is on white. The longest shots are the nav demo (3.5 s) and the principles row (2.5 s). The acceleration is the icon wall pull-back (#59–#62, 4 frames of 2× density jumps). Climax: "One Uber". Ending: subtraction to "One" to the logo, held ~2 s. There is no breath of empty black except #1.

## 7. What makes it premium
- **Every word is set to do what it means.** The type is the demo, so nothing needs a voice-over.
- The icons are proven **as typography**: they morph into letters, are typed with a caret, and sit inside a paragraph as words. That is the system's actual claim ("works with our typeface").
- Absolute restraint: black, white, one annotation blue. The only brand colour (Eats green) appears in the app carousel for 1 s.
- The ending subtracts words ("One Uber" → "One") until the logo is what's left.

## 8. Reusable techniques
1. **Self-describing adjectives.** For each claim word, pick the typographic property it names and animate that property: outline + construction grid (open), weight axis 900→100 (lighter), text-on-path with the Bézier relaxing V→U (friendlier), a left-to-right contrast ramp (accessible), step-and-repeat outlines (scalable). 1–1.5 s each, hard cuts between.
2. **Principle annotation accent.** Draw icons in black; colour only the segment that illustrates the principle being captioned, in one accent colour; remove all accents when the list completes.
3. **Growing row that keeps its width.** Each new tile slides in from the right; the whole row scales down so that the total width stays ~60% of the frame; the caption under the new tile fades grey→black.
4. **Icon → letter morph on a baseline.** Put the icons on a visible baseline at cap height, and morph each into a letter with a similar skeleton over ~2 frames (warning→A, refresh→C, pin→V, bubble→D), then type the next word from the same baseline.
5. **Selected-state walk.** Hold a UI crop still; step the selected state across a row of items once every 0.5 s. One changing variable, no camera move.
6. **Clipped-digit counter.** Digits roll vertically inside a line-height mask, with next/previous digits partly visible; the final digit lands last.
7. **Word subtraction to mark.** "One Uber" → drop "Uber" → "One" re-centres → the word is replaced by the logomark in the same position → the wordmark appends.
