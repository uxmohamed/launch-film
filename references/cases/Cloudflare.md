# Cloudflare (Workers Platform) — analysis (111 frames, ~55 s)

## 1. One-line concept
Cloudflare Workers Platform: "Everything we learned from powering 20% of the Internet → Start building." The film is one continuous **button-to-diagram** journey. A CTA pill is zoomed into until its arrow becomes a node on an infinite architecture canvas. The canvas pans through the use cases (workflows, AI, realtime/SFU, multiplayer, spikes), then zooms back out to a card, and the film closes on the wordmark and URL.

## 2. Visual world
- **Two grounds that alternate:** (a) saturated Cloudflare orange (#F6821F pushed to red-orange ~#FF4F0F), with a warm cream/yellow **radial glow rising from the bottom centre** (a sunrise, ~50% of frame width) plus a faint **scanline/CRT texture and a tiny dot-matrix grain**. (b) warm cream paper (#FBF6EE) with a faint dot grid. Orange scenes are used for statements; cream scenes for diagrams.
- **Type:** a geometric grotesk (Cloudflare's brand sans). Headlines are medium weight, and small (~3% of frame height) on the orange statements, giant only for the "Start building" pill (text ~12% of frame height at max zoom). Node labels are in a **monospace** ("Workflow", "Compute", "Instances ready with Cloudflare").
- **Imagery:** flat line-art architecture diagrams in the Figma-selection idiom: nodes are rounded squares with **corner handles** (the small squares at the corners of a selected frame), dashed icon insets, and dashed/dotted connector curves. Each product has its own colour: blue (Workers/Compute), green (Workers AI), pink/magenta (Storage/SFU/Media), orange (user/player nodes). Wireframe globe for "global".
- **UI staging:** almost no literal UI. Logos sit in a ghost browser tab strip (#40–46). The "Shipping with Cloudflare" card is a flat orange rectangle with a toast pill. Everything is flat, with no shadows, depth or 3D apart from the globe.
- **Motifs:** selection handles on every box, the bottom sunrise glow, dotted guide lines extending off-frame from UI edges (#83–84), and the cloud logo drawn as an outline.

## 3. Shot list
| Frames | ~s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–5 | 2.5 | Logo construction | orange field, thin crosshair guides | locked | guides split the frame (#1), then a 4-point spark star **draws from the centre** (#2), a bounding box draws (#3), and cloud arcs draw as construction circles inside the box (#4–5) | fills solid |
| #6–8 | 1.5 | Logo | solid cream cloud mark with the spark cut-out, ~40% of frame width | locked | fill snaps on (#6), the glow starts rising from the bottom (#7–8), and the mark **scales down** ~100→70% (#8) | the logo shrinks to a small icon above the text |
| #9–13 | 2.5 | Statement 1 | tiny cloud icon over "Everything we learned from" | locked | word-by-word add-on (#9 "Everything", #10 "+we", #11 "+learned", #12 "+from"), the line re-centring each time. #13 the words **blur out** (motion blur/defocus) | blur swap |
| #14–17 | 2 | Statement 2 | "powering 11% of the Internet" | locked | **number ticks 11% → 16% → 20%** (#14–16) while the text re-centres. #17 the "20%" dissolves into a dash (letters scatter) | line collapses to its centre |
| #18–20 | 1.5 | CTA reveal | "Start building" pill | locked, then push | the outer text blurs/collapses to the centre while a cream pill **expands from the middle** (#18 narrow, clipped "tart buildin") → full pill (#19) → pill 10% larger (#20) | continuous zoom |
| #21–25 | 2.5 | Zoom-through CTA | pill fills the frame | fast push ~3× then ~10× | #22–23 heavy **motion/zoom blur** plus chromatic doubling on the text. #24 the frame is all blurred cream with an orange circle. #25 sharp: the orange **→ arrow button** and a selected-frame outline with handles | the arrow becomes a node on the canvas |
| #26–31 | 3 | Canvas travel | arrow node → dashed curve → blue "Workflow" node → "Compute" group → green AI node | **continuous pan left/down** along the connector, ~1 node per second | nodes enter via the pan. Inside "Compute", the icons duplicate from 1→2→4 globes (#29→31) | pull out |
| #32–34 | 1.5 | Pipeline wide | Input "Start typing" → Workflow → Compute → Workers AI → Storage → output | **zoom-out** to ~25% of the previous scale. The canvas is now a bordered card (~90% of frame) | a side panel drawer appears lower right (#33–34) | cross-dissolve to the next diagram in the same card |
| #35–36 | 1 | SFU diagram | User A/B/C/D → Compute → SFU → Media | locked | the diagram swaps inside the same frame (a morph of the node layout), and the connectors redraw | swap |
| #37–39 | 1.5 | Durable Objects diagram | users → Workers → Durable Objects → Data & Storage → Coordinator. GET/POST labels | locked | the layout re-flows between frames (#37 and #38 differ) | cut to trust |
| #40–46 | 3.5 | Logo bar | "Trusted by" types on → "Trusted by the teams you trust". A ghost browser tab strip with ~20 customer icons | slow **push-in** (the frame widens ~15%) | the headline builds word-by-word (#40–42). The browser skeleton below scales up and fades (#44–46) | whole frame fades to cream |
| #47–52 | 3 | Headline morph | "Go from localhost → global in minutes" | locked; the line rises from lower third to centre (#47→51) | "localhost" and "global" arrive as **scrambled/glitch glyphs** (#48–50) that resolve by #51. "localhost" is pale orange, "global" solid orange | cut |
| #53–58 | 3 | Globe | wireframe orange globe with city lights, then close-up with app icons orbiting | slow rotate, then push to a horizon close-up (#56) | "Region: Earth" **decodes letter by letter** (#56 "Region:Dar h" → #57 "Region: Earth") | cut |
| #59–61 | 1.5 | Multiplayer | dot-grid, two labelled player cursors ("PLAYER 1/2") moving around a shared blurred image | locked | cursors move ~5% of frame per frame, and the image sharpens | cut |
| #62–63 | 1 | Node grid | a magic-wand AI node centred, database nodes on dashed rails | slight push ~5% | rails extend | cut |
| #64–65 | 1 | Chat bubbles | orange message bubble, tilted ~-8°, then a second paler bubble enters below | rotation settles | pop-in with overshoot | cut |
| #66–68 | 1.5 | Global request | wireframe hemisphere with a location pin → browser window; then two inputs → cloud node → browser | pan right | a dotted path draws from the pin to the window | cut |
| #69–72 | 2 | Let it spike | an orange area chart grows spikes, with a vertical dotted line at the peak and the mono label "812k Instances ready with CF" | **pull-out**: the chart frame goes from full-bleed to a card (#71–72) | the counter changes each frame (812k → 789k → 751k → 746k). The label is **typed on** | shrinks into a grid |
| #73–77 | 2.5 | "Fighting infra with 'cloud'" | a noisy cream log/waveform card full of error snippets ("High Latency", "Egress costs") | continuous **pull-out**: the card goes ~95% → ~45% of frame | static | slides left as the orange card enters from the right |
| #78–84 | 3.5 | Contrast card | orange "Shipping with Cloudflare" card with toast "Pushed 31 new updates today" | the orange card **slides in from the right over** the cream one (#78), covers it (#81–82), then zooms in on the toast (#83–84) | toast counter 31 → 40 | zooms through the orange |
| #85–92 | 4 | Build without boundaries | "Build without boundaries." centred, with small line-art product icons floating around it in selection frames | locked | icons **drift and rotate slowly** (~5°/s). Groups of icons cluster into selections (#88–91). #85 the text blur-sharpens in | defocus: the text ghosts up (#92) |
| #93–96 | 2 | Outline logo | the glow becomes **pixelated/mosaic** (#93) as the orange drains to peach, then cream. The cloud outline draws on (#93–95) | locked | stroke write-on, ~1 s | wordmark slides in |
| #97–100 | 2 | Lockup | outline cloud + "Workers" → "Workers Platform" in outlined letters | the logo shifts left to make room | "Platform" appends (#99) | cross-dissolve |
| #101–111 | 5.5 | URL | "workers.cloudflare.com" in orange on the cream dot grid | locked | #101 a slight baseline wobble on "cloudflare" (letters settling), then a hold | end |

## 4. Transition inventory
- **Construction-to-fill** (#1–6): guides → box → arcs → solid. It explains the mark's geometry.
- **Logo shrink to icon** (#8→9): the hero mark becomes a small "speaker" glyph above each statement and stays for #9–20.
- **Blur-out word swap** (#12→13→14): the old line defocuses while the new one arrives sharp.
- **Collapse-to-pill** (#17→18): the sentence contracts to its centre and a pill expands from the same point. The text becomes the button.
- **Zoom-through the CTA** (#20→25): the push goes through the pill's glyphs (motion blur plus RGB split) until the arrow alone remains, re-read as a node. This is the key idea, motivated by "Start building" → you're now building.
- **Canvas pan along the connector** (#26–31): the camera follows the dashed line, like a cursor tracing the graph.
- **Zoom-out to card** (#31→32, #71→72, #73→77): each deep scene shrinks into a bordered card, turning a "moment" into an "example".
- **Card slide-over** (#77→78): the orange "with Cloudflare" card slides over the cream "without" card, a before/after wipe.
- **Scramble decode** (#48–51, #56–57): text resolves from random glyphs.
- **Pixelate-dissolve** (#92→94): the orange glow breaks into a coarse mosaic (~40px blocks) and fades to cream. A digital "dissolve".
- **Outline write-on logo** (#93–96), then a wordmark push (#97–100).

## 5. Easy-to-miss details
- The bottom glow is present in every orange statement scene and in the same spot, so it acts as a stage light. It **pulses larger** as the CTA arrives (#18–20).
- The scanline texture is visible on the orange only. The cream scenes are clean apart from the dot grid.
- Number tick (#14–16): 11 → 16 → 20 across ~1 s with ease-out (the jumps shrink). The sentence width changes and re-centres live.
- In #22–23 the "Start building" text has a **~1.5% RGB/ghost offset** during the zoom, which sells the speed.
- The selection handles on the arrow frame (#25–27) persist as the camera pans. That's the Figma idiom: "you are editing this".
- In Compute (#29→31) the icon count doubles per beat (1 → 2 → 4) to show scaling without words.
- Counters appear in three places: the % stat, the "Instances ready" count, and "Pushed 31→40 updates". Every proof point is a moving number.
- The "Let it spike" label's number *decreases* between frames while the chart grows. It's likely a live-looking random ticker rather than a narrative count, so it feels live.
- Headline "localhost → global": the arrow glyph is typed, and the colour weight goes pale → saturated to encode the before/after.
- The card zoom-outs always land at ~45–50% of frame width, with the next element entering in the freed space.
- The URL end card holds ~5.5 s, very long, and the orange has been completely drained from the ground by then.

## 6. Pacing curve
It opens medium (2.5 s logo build), then accelerates through statements (~1.5–2.5 s each) into the **zoom-through at ~10–12 s, the energetic peak**. 13–20 s is fast canvas travel (1–1.5 s per diagram). The logo bar (20–23 s) is a breather. 24–46 s is a rapid montage of use-case vignettes (1–2 s each; this is the densest part, 12 micro-scenes). 43–46 s is the before/after card (the argument). 46–50 s, "Build without boundaries", slows down with floating icons. The film closes with the outline logo and ~5.5 s of URL: a long, calm, clean landing.

## 7. What makes it premium
- **One-take logic**: the CTA is literally the door into the product world. The zoom-through is timed so the arrow's circle becomes the first node, with no cut.
- A strict dual palette (orange = voice/claims, cream = product/diagrams), switched with purpose.
- Diagrams are presented as *editable* design objects (selection handles, dashed insets), which speaks to builders.
- Every claim has a moving number (20%, instances, updates), a motion-native kind of social proof.
- Analogue-ish texture (scanlines, grain, glow) on a flat vector brand keeps it from looking like a slide deck.

## 8. Reusable techniques
1. **CTA zoom-through**: pill expands from its centre (0.3 s), holds 0.5 s, then an exponential push ~12× over 1 s with directional blur and a 1–2% RGB split at peak velocity. Land on a glyph (arrow/icon) that becomes the first element of the next scene.
2. **Stat ticker in a live sentence**: animate a number in 3–4 discrete steps over ~1 s with ease-out, and re-centre the line each step (don't reserve width).
3. **Canvas-follow-the-wire**: camera tracks a dashed connector at ~one node per 0.8–1 s. Nodes carry selection handles. Finish with a zoom-out of ~4× to reveal the whole pipeline inside a bordered card.
4. **Deep-scene → card shrink**: scale the full-bleed scene to ~45% into a thin-bordered card over ~1 s ease-in-out, then slide a contrasting card over it from the right (before/after).
5. **Scramble-decode keywords**: only the key nouns (localhost, global, Earth) scramble through random glyphs for ~3–4 frames at 24 fps-equivalent ×2 before resolving. The rest of the line is static.
6. **Sunrise stage-glow**: a radial warm gradient anchored at the bottom centre, ~50% of width, sitting under all statement text. Swell it +15% on the CTA. End by pixelating it (mosaic ~2% of frame width) as it fades.
7. **Construction-line logo build**: crosshair guides → bounding box → arcs → solid fill over ~2.5 s, then shrink to an icon (~15% scale) that persists as a header glyph over the statements.
