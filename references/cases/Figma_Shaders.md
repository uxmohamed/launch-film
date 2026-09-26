# Figma — Shaders (101 frames ≈ 50 s)

## 1. One-line concept
Figma launches shader fills and effects: prompt a custom shader, stack multiple shaders on a layer, and apply them as fills. The spine is **"Shape your own shaders" → a demo of one prompt → a demo of stacking → a demo of fills → "Prompt them. Stack them. Share them."** It ends by running the Figma logo *through* the shaders. The film is its own proof: almost every frame is a shader output.

## 2. Visual world
- **Two alternating grounds:**
  - pure black for the title and outro acts (#1–#15, #79–#101);
  - Figma's light-grey canvas (#16–#78), where shader output fills the frame edge-to-edge and the Figma **floating shader panels** sit on top.
- **Palette:** deliberately loud and variable, because each shader brings its own: acid yellow, riso orange, electric blue, magenta, lime and olive. The only constant colour is **Figma blue (#0D99FF)** for UI accents: the send button, selection handles, the typed prompt's newest characters, and the headline "Shape your own shaders".
- **Type:**
  - Figma's grotesk (Whyte-like) at medium weight for headlines, ~8% of frame height, in blue (#12) or acid yellow (#79–#83), with tight tracking.
  - UI panel text is small (~1.8%).
  - Demo artwork uses big heavy display type ("MUSEUM OF SPECULATIVE FUTURES", "PEDAL CLUB", "M✱SF", "FACILITATE CONNECTION"). This is fictional client work that makes the shaders look useful rather than decorative.
- **UI staging.**
  - The Figma editor appears **once in full** (#16–#19). The screen's edges show a blue-striped scanline shader treatment (#17–#19), so even the orientation wide is "shaded".
  - After that: **macro panels only**, meaning a single floating property panel ("Organic distortion", "Gradient Map", "Particle Grid", "Riso print", "Shader fills") at ~25–30% of frame width, white, with a very soft shadow and radius ~12 px, over full-bleed artwork.
  - The cursor is large (~4% of frame height), black with a white outline.
- **Motifs:**
  - **Stacked effect pills**: collapsed panels cascade diagonally (#39–#43, #71–#78), each offset ~3% down and right. The stack visualises "stack them".
  - The M✱SF asterisk-node logo.
  - Dot and halftone grids.

## 3. Shot list
| # | Dur | Shot | On screen | Camera | Animation | Exit |
|---|---|---|---|---|---|---|
| 1 | 0.5 s | Tile | A tiny dark flower silhouette on a green square, ~20% width, centred on black | static | — | more tiles slide in |
| 2–5 | 2 s | Tile carousel | The same flower rendered three ways (etched line / pink watercolour / yellow halftone) as tiles **sliding right-to-left** | truck left | each tile is a different shader; the tiles overlap by ~10%; the red in the watercolour tile spreads (#3 → #5) | tiles collapse |
| 6–10 | 2.5 s | Tile collage | New tiles pop in: a dot-strip pattern (#6), an orange column pattern (#7), blue pixel mosaic (#8–#9), all **overlapping and cascading** diagonally | slight drift | each new tile enters at ~40% width and pushes the previous ones up-left | the collage rearranges into a frame for the headline |
| 11–15 | 2.5 s | Headline over collage | "Shape" (white, #11) → "Shape your / own" (blue, #12) → "Shape your / own shaders" (#13); the tiles sit at the corners (flower TL, bicycle TR, mosaic BC) | static | **word-append; the first word is white, then the line turns blue** as it completes. Tiles keep animating (the mosaic flickers #13 → #15) | hard cut to the Figma UI |
| 16–19 | 2 s | Orientation wide | The Figma editor with a cloud photo selected; a blue scanline shader bleeds from the screen edges (#17) | **push ~1.1×** (#16 → #17) | cursor moves to the selection's top-right handle (#18–#19) | push to the prompt box |
| 20–24 | 2.5 s | Macro prompt | Prompt card: "Can you make a custom organic distortion effect?" | **push ~3× onto the card** (#20) | typed ~12 chars per 0.5 s; **the newest ~6 characters are Figma blue**, then turn black (#21 "a c", #22 "organi", #23 "on effe") | cursor clicks send (#24) |
| 25–30 | 3 s | Macro panel on output | The "Organic distortion" panel appears over full-bleed clouds; sliders Displace 0% → 70% → 100%, Noise 3, Angle 45°, Blur radius 3 | camera re-centres on the panel (#25 → #26) | **the cloud image distorts live** as Displace increases (#26 crisp → #27 smeared → #28 heavy swirl); the cursor drags each slider in turn | cut |
| 31–36 | 3 s | Gradient Map | A portrait in green/orange; the Gradient Map panel with Offset 85 → 37 → 23 → 20 | panel slides in from the bottom-left (#31 → #32), then moves (#36 at left-bottom) | the image's colour mapping **shifts continuously** pink → olive → yellow → orange as the offset slider drags | cut |
| 37–44 | 4 s | Stacking | A galaxy image; collapsed pill "Gradient Map" (#37–#38), then a second pill stacks (#39), then "Particle Grid" (#40–#41, the image becomes a pixel column grid), then "Riso print" (#42–#43, the grid becomes orange/blue riso blocks) | the image window shrinks from full-bleed to a rounded card (#39) | each new pill **drops in on top of the previous one, offset down-right**, and the effect applies instantly; a name is typed into each pill ("G…" → "Gradient Map", "Riso prin…" in blue) | the card becomes a poster in a carousel |
| 45–46 | 1 s | Carousel | Three poster cards ("Between Two Forecasts VOLUME IV") with different treatments | truck left | — | cut |
| 47–49 | 1.5 s | Fill panel macro | Orange artboard with a black ":SF" logo; the right panel: Fill → "Dither waves 100%" | locked | cursor clicks the Dither waves fill row (#48 → #49, highlight) | the Shader fills picker opens |
| 50–56 | 3.5 s | Shader fills picker | "M✱S" logo on an artboard; picker grid: Dither waves, Fluid halftone, Particle web, Magnetic field | locked | **hovering each thumbnail swaps the artboard background live**: orange blank (#50) → grey/orange dither waves (#51–#53) → orange halftone dots (#54–#56) | cut |
| 57–59 | 1.5 s | Output | "MUSEUM OF SPECULATIVE FUTURES" in yellow-boxed type on light blue with particle-web lines, "Plan your visit" button | slight push | the particle web lines **move** (the nodes drift between frames) | pull back |
| 60–62 | 1.5 s | Pull-back | The same design as a website on a **grey noise-texture ground** ("Welcome to the Museum of Speculative Futures") | **pull-back ~2.5×** | — | cut |
| 63–65 | 1.5 s | Line Boil | A hand-drawn eye with **blue selection handles** over a sepia collage | static | the "Line" pill is typed → "Line Boil"; the eye's strokes wobble per frame (a boil) | cut |
| 66–69 | 2 s | Macro "OWN" | Huge "OWN" type on olive, then a "Dither" pill over a grainy photo of reeds | truck | the dither applies to the photo (#67 → #69 grain changes) | cut |
| 70–72 | 1.5 s | PEDAL CLUB | A poster with a blotchy purple-edged ink shader; stacked pills Outlines / Metaballs / Distance Field | static | pills cascade in (#70 two → #71 three) | cut |
| 73–75 | 1.5 s | Member card | Magenta "M✱SF MEMBER" card; pills Outlines, Metaballs → then 3D Extrude, Fluted Glass | truck left: the card is part of a row (#74) | the card surface changes (flat magenta → fluted-glass orange gradient) | cut |
| 76–78 | 1.5 s | Max stack | "FACILITATE CONNECTION" with 7+ pills floating (Color Adjust, Fluted Glass, 3D Extrude, Film Grain, Particles, Noise Displacement) | slight push | pills **accumulate to fill the frame**: an effect-stack density peak | hard cut to black |
| 79–80 | 1 s | Type | "Prompt them." acid yellow on black | static | **the text is revealed through a shader**: at #79 "them." is a smeared, painterly blob that resolves at #80 | word-append |
| 81–82 | 1 s | Type | "Prompt them. / Stack them." → "+ Share them." | static | each line appears in turn, re-centring vertically | shader dissolve |
| 83–85 | 1.5 s | Type → shader | The three lines **glitch and halftone** (#83 horizontal smear), become a big dot grid (#84), then a green/black dot matrix (#85) | — | the text itself gets shaded out | the logo emerges |
| 86–95 | 5 s | Logo through shaders | The Figma logo rendered through ~8 shaders in sequence: 3D extruded side view (#86), green pixel mosaic (#87), white dotted outline (#88–#89), blue/orange scanlines (#90), with a **ring outline** (#91), magenta dot matrix (#92–#94), full-blue scanline field with the logo embossed (#95) | static, centred; the logo's size is fixed at ~20% of frame height | ~0.5 s per shader; every frame is a new treatment | the shaders resolve |
| 96–101 | 3 s | End card | The standard Figma logo in full colour, ~20% height, on black | static | #96 still has a slight halftone fringe on the green circle's edge; clean by #97 | end |

## 4. Transition inventory
- **Tile carousel slide (#1→#5):** a side-scrolling row of shader variants of one image. It establishes "one input, many shaders".
- **Collage → headline frame (#10→#11):** tiles settle to the corners, making space for type.
- **Hard cut black → Figma UI (#15→#16),** softened by the shaded screen edges.
- **Push into the prompt box (#19→#20),** motivated by the cursor reaching the AI affordance.
- **Send → panel over output (#24→#25):** the prompt card's result is the panel plus the effect. It's the prompt → result pattern, where the output fills the frame and the panel is the only UI left.
- **Live-parameter scrubbing** replaces cuts: within a shot the artwork transforms continuously as sliders move (#26–#28, #32–#36). The "verb transition" is the product's actual control.
- **Full-bleed → card (#38→#39):** the image shrinks into a rounded card as the stack grows. It's the "scene → card" pattern.
- **Hover preview swaps (#50→#56):** the picker thumbnails drive background changes, so a hover is the cut.
- **Output → context pull-back (#59→#60):** a macro poster to a full website mockup.
- **Hard cuts between demo artworks (#62→#63→#66→#70→#73→#76),** with carriers: the pill UI stays in the same visual language, and the pill count increases each time (1 → 2 → 3 → 4 → 7+).
- **Text through a shader (#79, #83–#85):** the headline itself is processed, and dissolves into a dot matrix that becomes the start of the logo sequence.
- **Logo shader riffle → clean logo (#86→#96):** fixed position and size, with the treatment swapping every 0.5 s. It's a fixed-layout slideshow where only the material changes, then it lands on the clean brand.

## 5. Easy-to-miss details
- **Arrival state = Figma blue on the newest typed characters** (#21–#23), and again in pill names ("Riso prin", "Line", "Di"). The newest ~5 characters are blue and turn black after about 0.5 s. That's the manual's "hot text", using the brand's UI blue.
- The headline's first word "Shape" is white (#11). When the line completes, **the entire line turns blue** (#12–#15). Colour arrives on completion, not per word.
- Sliders show **real values ticking** (Displace 0% → 70% → 100%, Offset 85 → 37 → 23 → 20). The artwork changes on the same frame.
- The collapsed pills show a **ghost of the pill underneath** (#39–#43: a second pill peeks out ~3% down and right, with its label cut off), so the stack is legible as depth.
- Selection handles (blue squares, #63–#65) are drawn over art to remind the viewer that this is an editable canvas, not a render.
- The pill-count escalation is 1 (#25) → 1 (#31) → 2–3 (#39–#43) → 3 (#70–#72) → 4 (#74–#75) → 7+ (#76–#78). That's a density ramp toward the outro.
- The final Figma logo's edge retains a halftone fringe for one frame (#96) before going clean. It's a one-frame "residue" of the effect.
- The Figma logo shader riffle keeps an **exact centre and size** across all 10 treatments. The change is purely material.

## 6. Pacing curve
- Fast open: tiles every 0.5 s for 5 s, then the headline at 7.5 s.
- Demos run at a 1.5–4 s cadence, with the prompt demo the slowest (5.5 s for prompt plus slider). They speed up to about 1.5 s per artwork in the "stack" montage (#63–#78).
- There's no real breath until the black type outro (#79–#82).
- The climax is the text dissolving into a dot matrix and the logo shader riffle (#83–#95, 6.5 s).
- The ending holds the clean logo for 3 s.

## 7. What makes it premium
- **The effect is the film's texture and its transitions**: tiles, title, UI edges, outro text and logo are all shaded. There is no neutral ground that isn't made of the product.
- Demo content is **art-directed fictional client work** (a museum, cycling club, membership card, forecasts poster) with real type systems. It shows shaders applied to design, not a shader playground.
- UI is reduced to a single floating panel at macro scale. The editor chrome is shown once for 2 s.
- The stack visual (cascading pills) makes an abstract feature ("combine effects") literal and countable.

## 8. Reusable techniques
1. **Same input, many treatments carousel.** One image rendered N ways as tiles sliding horizontally with a 10% overlap, one tile per 0.5 s. It's the opener for any "styles/filters/effects" product.
2. **Live-scrub instead of cut.** Keep the panel at 25–30% of frame width over full-bleed output, and drag one slider across 1–1.5 s while the output transforms on the same frames. Show the value text ticking.
3. **Cascading pill stack.** Collapsed effect pills stack with a +3% x/y offset; each new pill drops in 0.5 s after the last and applies its effect instantly. Escalate the count across the act (1 → 2 → 3 → 7).
4. **Hover-driven background swap.** In a picker, each hovered thumbnail replaces the canvas background on the same frame. The cursor travels thumb to thumb at ~1 per second.
5. **Headline turns brand colour on completion.** Words append in white; the frame the last word lands, the whole line recolours to the brand accent.
6. **Type → product-process dissolve.** The closing tagline is itself run through the product's effect (smear → halftone → dot matrix, 1.5 s), and the matrix resolves into the logo.
7. **Logo material riffle.** Hold the logo at a fixed centre and size and swap its rendering every 0.5 s for 8–10 variants, then the clean mark for 3 s, with a one-frame residue of the last effect.
