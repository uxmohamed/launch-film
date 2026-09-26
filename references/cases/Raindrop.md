# Raindrop — analysis (100 frames, ≈50 s)

## 1. One-line concept
Raindrop Signals 2.0 is a frontier classifier ("rd-signals-2") that monitors AI-agent behavior in production. The spine is a manifesto in monospace: Introducing → benchmark proof (precision/recall, 99.93% lower cost) → Track anything across millions of events → via UI / via API → Zero Data Retention → a worked example ("every tool call fails, but the agent says it succeeded") → train/host/run/evaluate → online learning loop → "Stop paying for judges. Start using signals." → raindrop.ai.

## 2. Visual world
- **Background:** deep teal-navy (~#0D2230) with a faint dot-grid/character noise texture across the whole frame. The texture density changes to signal state: sparse at rest, dense "character rain" at #29 and #71–#74.
- **Type:** a monospace (Berkeley/JetBrains-Mono-like), regular weight, white. Headlines ~2.5–3% of frame height (e.g. "Introducing Signals 2.0" is ~33% of frame width). There is one giant exception: "Track" at ~40% frame width (#26). Key words appear **inverted** (white block, dark text), like a terminal selection. The final URL "raindrop.ai" switches to a rounded sans, the only non-mono type.
- **Imagery:** everything is **ASCII/dot-matrix rendered**: spheres made of characters with horizontal scan banding, bars that dither from characters to solid, a raindrop logo made of characters, a ring "flywheel" of dots. No screenshots. UI (signal card, match list, terminal, code) is redrawn in the film's own mono system.
- **Depth:** flat, with no shadows. Depth comes from opacity layering (dim background code at ~15–25%, active lines at 100%) and from bloom on white bars (#67).
- **Motifs:** the ASCII sphere (classifier/model), the inverted word block, bracketed tags `[ MATCHED ]`, tiny corner labels (bottom-left brand label on every frame from #6).

## 3. Shot list
| Frames | ≈s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1 | 0.5 | Empty | textured navy | — | — | type |
| #2–#5 | 2 | Title | "Introducing [glyph]" → "Introducing Signals 2.0" → + "powered by rd-signals-2" | locked | the product name decodes from a scrambled glyph (#2) in one beat; subline fades in (#4) | cut |
| #6–#7 | 1 | Sphere + line | "a frontier classifier" over an ASCII sphere (~30% frame width) | locked | sphere rotates: band pattern changes each frame | text swap |
| #8–#10 | 1.5 | Word build | "[for]" inverted at left → "for agent behavior" centered | locked | new word appears inverted, then the line re-centers and un-inverts; the sphere's texture goes from banded to noisy | swap |
| #11–#14 | 2 | Header + morph | "[Frontier]" top-left → "Frontier  model  performance" with wide word gaps (#12) | locked | the sphere compresses into a rectangular stack of horizontal bars (#13–#14), a sphere-to-chart morph | chart forms |
| #15–#20 | 3 | Bar chart | "Precision" and "Recall" columns; model rows; rd-signal-2 row | locked | bars resolve from dithered ASCII to solid grey (#15→#18); "Recall" header fades from grey to white (#16→#17); the rd-signal-2 bar goes solid white with inverted label (#17, #19) | cut |
| #21–#22 | 1 | Macro chart | "RELATIVE COST · lower is better"; huge zoomed label "Claude Son|" typing + "$" (#21) → zoomed rows with "36x / 1x" (#22) | extreme close-up (~3×) | labels type in | zoom out |
| #23–#25 | 1.5 | Full chart | full cost bar chart; "cost [99.93% lower]" in an inverted block | pull back ~3× in one beat | multipliers **tick up** (581x→1604x→1658x; 642x→1580x→1600x; 175x→268x) as bars extend; inverted text types letter by letter (#23 "lo", #24 "lower") | cut |
| #26 | 0.5 | Giant word | "Track" huge with one glitched glyph ("c" ↔ ":") | — | glyph scramble | shrink |
| #27–#28 | 1 | Tag cloud | "Track anything" small center + ~20 outlined pill tags (event names) scattered | locked | tags fade in; some turn white-filled (#28) | rain |
| #29–#30 | 1 | Texture | "across millions of events a day" + vertical columns of streaming characters | locked | character rain peaks (#29) and fades (#30) | swap |
| #31–#32 | 1 | Line | "through our U[glitch]" → "through our UI" | — | decode | text flies to header |
| #33–#38 | 3 | Product UI | header "through our UI" top-left; "0 events" counter; NEW SIGNAL card typing the quote "the agent says it transferred the user to a human, but the transfer never happened" + "Create signal" / "Keep refining" | locked | quote types (#33→#34); card collapses to a progress bar (#35); counter ticks 0 → 0.1m → 0.7m → 1.5m → 1.7m (top-right, large) with an orange-spiked histogram; match cards with MATCH/NO MATCH stack in | cut |
| #39–#43 | 2.5 | Terminal | CLI log: "> create a signal in production where…", tool calls, scanning counts | log scrolls up; text shrinks (#40) | lines stream; "[Or via]" → "[Or via our API]" + "[with]" inverted blocks bottom-left | cut |
| #44–#46 | 1.5 | Sweep | "[Zero Data Retention]" inverted, center | locked | a vertical column of glowing characters sweeps left → right across the frame (~40% of the width per frame) like a scanner | cut |
| #47–#50 | 2 | Example line | "every tool call fails," → "[but]" inverted → "…but the agent says it succeeded" | locked | the second line builds under the first; the pair re-centers | pull-in |
| #51–#53 | 1.5 | Code | the sentence becomes a code comment/header; function `repeatedWithoutChange = attempts.length >= 3 && haveIdenticalInputs(...) && attempts.every(call => call.failed)` + `return classify("silent-retry", …)`; right column tags `[3 CALLS] [IDENTICAL] [EVERY TOOL FAILS] [NO MODEL CALL] [MATCHED]` | locked, then push | active lines at 100%, others ~25%; "silent-retry" inverted (#53) | zoom |
| #54–#56 | 1.5 | Macro code | code cropped at ~1.8×, left-cut | push-in then drift | code dims out (#55); the right-hand tags remain, `[ MATCHED ]` inverted; faint ASCII spheres fade in | cut |
| #57–#58 | 1 | Constellation | several ASCII spheres with tiny labels, connector lines, square selection brackets, a ray to the right | locked | spheres fade out, leaving labels (#58) | cut |
| #59–#63 | 2.5 | Train/host | "Train and h[glitch]" → "Train and host custom classifiers in seconds" (left); ASCII sphere with ring (right); small code panel far right | slow | code panel grows as the sphere shrinks (#61→#63) | cut |
| #64–#67 | 2 | Experiments | "Run exp[" → "Run experiments" with 5 ASCII spheres around it | locked | spheres redistribute to 4 corners (#66); the text becomes a glowing white redaction bar with bloom (#67) | bar becomes scanner |
| #68–#70 | 1.5 | Evaluate | "Evaluate [offline]"; a tall white vertical bar at left sweeps right (#69), revealing a large ASCII sphere with outer ring | the bar wipes across | wipe reveal | cut |
| #71–#74 | 2 | Online learning | "And with" → "And with online learning" over a character field that densifies each frame | locked | texture density ramps ~4× | decode to title |
| #75–#77 | 1.5 | Name | "Rai[glitch]" (larger, left) → "Raindrop Signal[glitch]" → "Raindrop Signals" centered | locked | letter decode | cut |
| #78–#81 | 2 | Flywheel | "gets better wh[" → "gets better while you sleep" in a ring of dots with 6 spokes; labels deploy / sample / evaluate / find regressions / retune / re-evaluate | slow rotation | labels fade in around the ring | cut |
| #82–#84 | 1.5 | Line | "Stop [paying]" → "Stop paying for judges"; a few tiny square nodes appear | — | inverted-word build | swap |
| #85–#89 | 2.5 | Line + swarm | "Start [using]" → "Start using signals" with an increasing swarm of labeled square nodes (≈5 → ≈60) | locked | nodes multiply each frame; some have tiny cursors/arrows | clear |
| #90–#95 | 3 | CTA + logo | "Try it" → "Try it now a[" → "Try it now at" over an ASCII raindrop logo shape; text leaves and the logo holds, then dims (#94–#95) | locked | logo resolves from noise; swirl detail | cut |
| #96–#100 | 2.5 | URL | "raindrop.ai" in sans, center | locked | hold | end |

## 4. Transition inventory
- **Glyph-decode in place** (#2, #26, #31, #59, #64, #75–#76, #78, #91): the newest word/letters show random glyphs for one beat, then resolve. This is the film's main text entrance, used ~10 times.
- **Inverted-word build** (#8, #11, #23, #41–#42, #44, #48, #82, #85): each new key word lands in a white block, then the line re-centers and the block drops. It works as an emphasis-then-settle.
- **Sphere → chart morph** (#12→#15): the character sphere is re-binned into horizontal bars. The model *becomes* its benchmark.
- **Macro-to-full pull-back** (#22→#23): starting at an unreadable ~3× crop of the cost chart, then snapping out to reveal the whole comparison.
- **Line-to-header relocation** (#32→#33, #50→#51): a centered statement moves to the top-left and becomes the section header of the UI/code that follows.
- **Scanner sweep** (#44→#46, #68→#69): a vertical bright column wipes across, revealing the next state.
- **Bloom bar transition** (#66→#67→#68): the headline text turns into a glowing redaction bar, which becomes the vertical scanner of the next shot.
- **Texture density ramp** (#71→#74): background character noise densifies to feel like a data flood, then resolves into the product name.
- **Swarm build** (#85→#89): nodes multiply behind the claim, then hard cut to a near-empty "Try it".
- **Logo from noise → font switch** (#93→#96): the ASCII raindrop gives way to a clean sans URL.

## 5. Easy-to-miss details
- The bottom-left micro brand label appears on nearly every frame from #6, like a persistent watermark/HUD.
- "Frontier  model  performance" (#12) is set with double word gaps, so the words look like separate tokens being placed.
- In the precision chart, the rd-signal-2 bar is the *only* solid white bar (the others are grey). Emphasis comes from luminance, not position or color.
- Counters tick with a sub-second increment (cost multipliers ×2.7 in one beat; events 0.1m→1.7m over 2 s), and the bars grow in sync.
- The orange spikes in the events histogram (#36–#38) are the only warm color in the film, reserved for anomalies/matches.
- Code scenes use opacity focus: 3 active lines at 100%, surrounding code ~20–25%, with bracket tags aligned right as "evaluation output".
- The ASCII spheres always have horizontal scan-band structure; their rotation is implied by the bands changing each frame, not by visible spin.
- The glowing bar in #67 has a ~20 px bloom halo at 1920. It is the only bloom apart from the scanner bars.
- The inverted block types letter by letter *inside* the block (#23 "99.93% lo" → #24 "99.93% lower"), with the block width fixed to the final width.
- Ending: the raindrop logo is dimmed to ~40% before the cut to the URL, so the logo recedes and the URL reads as the final word.

## 6. Pacing curve
It is very dense: ~25 distinct text beats in 50 s, i.e. a new beat every ~2 s. The film opens fast (title in 2 s), puts proof up front (benchmarks by 12 s), then keeps a constant 1–2 s cadence through the feature list. It breathes three times: the NEW SIGNAL/counter UI (3 s), the code example (4 s), and the flywheel (2 s). Density climaxes at the node swarm (#85–#89), then drops to near-silence for "Try it" and a 2.5 s URL hold. The rhythm is set by text decode beats rather than camera moves; the camera is almost always locked.

## 7. What makes it premium
- A complete, self-consistent rendering language (mono + ASCII + inverted blocks) applied even to charts, UI, and the logo. There is no stock screenshot anywhere.
- The benchmark is staged cinematically (macro crop → pull-back → counters) rather than as a slide.
- A concrete failure example written as a sentence, then as code, then as tags, which shows *how* the classifier thinks.
- Color discipline: white/grey on navy, with orange only for anomalies.
- Texture density is a narrative variable (quiet vs "millions of events").

## 8. Reusable techniques
1. **Glyph-decode word entrance.** The last 2–4 characters of a new word cycle through random glyphs for 1–2 frames (~0.1 s each at 24 fps), then resolve. Set in mono so the width never jitters.
2. **Inverted-block emphasis then settle.** A new key word appears in a white block (padding ~0.3 em). After 0.5 s the block drops out as the full line re-centers (0.3 s ease-out).
3. **ASCII primitive → data viz morph.** Render the "model" as a character-sphere with scan bands; re-bin its characters into horizontal bars, then dither the bars to solid over ~1.5 s.
4. **Macro-first chart reveal.** Open at 3× on a label mid-type, then snap out to the full chart while numbers tick to their finals (ease-out, ~1 s).
5. **Statement → header → artifact.** A centered claim moves to the top-left as a header, and the UI/code demonstrating it builds below. The claim stays on screen as context.
6. **Opacity-focus code.** Dim the whole snippet to 20–25% and light only the lines being explained. Right-align bracket tags that tick on one per 0.25 s.
7. **Scanner sweep wipe.** A vertical bright bar (or column of glowing characters) crosses the frame in ~1 s, revealing the next state behind it.
8. **Density ramp as climax.** Multiply background particles/nodes 5–10× over 2 s behind the key claim, then hard-cut to a near-empty CTA frame.
