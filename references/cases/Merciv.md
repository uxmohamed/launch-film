# Merciv — analysis (161 frames, ≈80 s)

## 1. One-line concept
Merciv is a consumer-research AI for brands. It takes one question ("Where are there gaps in the Skincare market on TikTok that major brands aren't positioned to fill?"), and the film follows it all the way through: brand thesis → typed query → sources counting up → cited answer → tracker set up → an alert arrives → files exported → shared in Slack → logo. There is no voiceover-driven UI. Every beat is a UI micro-moment staged on warm off-white, with short kinetic-type interstitials.

## 2. Visual world
- **Background:** warm off-white (#F8F6F1-ish, paper). Two exceptions: the logo reveal on deep petrol teal (#16404D-ish) with a faint dot-grid and twinkling specks (#27–31), and one sky-and-clouds backdrop for the first UI overview (#32–33).
- **Dot-grid motif:** a faint 1 px dot matrix appears on the teal logo card and on the "Data changes fast" card (#78–84). Red dots scattered across it are "data points". Later the same red dot becomes the "o" in "Always on" and grows into the broadcast/alert icon (#110–116).
- **Type:**
  - Interstitials use a small monospaced-feeling grotesk at ~1.5% frame height (#4–20, "Every great brand"), tiny and centred, with huge negative space.
  - The contrast beat "keeping up is harder than ever" is a rounded geometric sans at **~25% frame height** (#21–22), then shrinks as more words stack (#23–24).
  - UI type is rendered large, cropped macro (#37–47: the input field fills the frame, text ~5% height).
- **Imagery:** editorial fashion and beauty photography (studio product shots, film-grain portraits, fabric swatches) placed as flat rectangles, no shadow, on paper.
- **UI staging:** almost always **flat, borderless, cropped macro**. The camera sits inside the app at 2–4× zoom and follows the cursor or caret. No device frame, no tilt. Card shadows are very soft (~20 px, 5% opacity). The accent colours are Merciv coral/red (#E8553F) and teal highlight chips ("Skincare").

## 3. Shot list
| Frames | ~s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–3 | 1.5 | Empty paper | nothing | static | — (deliberate held blank) | — |
| #4–6 | 1.5 | Tiny type | "Every" → "Every great brand" | static | Words appear one at a time, hard on (no fade visible) | Photo appears *behind* the text |
| #7–10 | 2.0 | Photo swap under text | Green clay texture → folded sweaters → linen shirt → product basket | static | Each photo replaced every frame (0.5 s), and each has a slightly different aspect ratio (~0.36→0.40 frame width). The text stays white-on-photo | Photo removed, the text changes |
| #11–13 | 1.5 | Tiny type | "needs" → "needs to understand" → "needs to understand its consumer" | static | Word-by-word append; the string re-centres each time | Photos enter from the edges |
| #14–18 | 2.5 | Collage build | Portraits pop in at edges (#14 one, #15 three, #16 eight) then fill the frame (#17) | slight push | Photos appear at edges first, then **overlap and fill inward**. At #17 a central hero portrait sits on top | #19: all but the hero vanish |
| #19 | 0.5 | Hero isolated | Single portrait centred | — | Surrounding collage removed in one frame | Cut to type |
| #20 | 0.5 | Tiny type | "But today," | — | — | Hard cut to giant type |
| #21–24 | 2.0 | Giant type stack | "keeping / up / is / harder / than ever" | **zoom-out** as the stack grows | Each new word is added below and the whole block scales down to fit (25% → 8% height per line) | Type collapses to a black dot |
| #25–26 | 1.0 | Dot | A black dot, ~6% height, moves from right-centre to left-centre | — | Dot slides ~40% of frame width | Dot shrinks to a pixel as the BG floods teal |
| #27–31 | 2.5 | Logo on teal dot-grid | The dot becomes the first bar of the logomark "\|i·ıl"; bars grow; "M" → "Merciv" types out | static; the logo drifts left→centre | Logomark bars grow up from the dot. The wordmark types letter-by-letter (#29 "M", #30 full) | Hard cut to UI over sky |
| #32–33 | 1.0 | UI establishing | Full app window floating on a cloud sky | static | Home view then scrolled content | Cut to macro |
| #34–36 | 1.5 | Macro, UI on paper | "What are you making sense of today?" prompt box | push in ~1.1→1.3 | The caret starts typing "Wh…" (#36) | Hard zoom cut to 3× |
| #37–47 | 5.5 | Macro typing | "Where are there gaps in the [Skincare] market on / → [TikTok] that major brands are…" | **camera tracks the caret** horizontally; text runs out the left edge | Typewriter ~6–8 chars per frame. "Skincare" auto-tokenises into a teal highlight (#40–41). "/" opens a source menu (Reddit, TikTok, Instagram, Amazon); the highlight moves Reddit→TikTok (#43–44); the TikTok chip inserts (#45) | Zoom-out to the full prompt box |
| #48–50 | 1.5 | Prompt box wider | "Happy Monday, Sophie." greeting; the full query in the box; cursor moves to the red send button | zoom out ~0.4× | The cursor arrives and clicks (the send button turns darker, #50) | The prompt collapses into a pill |
| #51–55 | 2.5 | Query pill | The query as a single pill; "Thinking" with a sparkle spinner below-left | static, tiny scale | The pill shifts slightly up. "Thinking" fades in (#53) and out (#55) | Cut to bottom-cropped source ticker |
| #56–65 | 5.0 | Source counter macro | "Web Search 9 sources" → "Product Search 84 → 305 → 737 → 930 → 1009 → 1028 sources"; "1782 considered" | the camera sits low in the frame, then **pulls up and out** (#64–65) | The step label cross-fades per frame with a letter-scramble (#57 "…b Search", #58 "Kr…ledge Search"). The icon stack in the source pill swaps favicons. The count ticks | Pull back reveals the query above; answer text starts below |
| #66–69 | 2.0 | Answer scroll | The long cited answer with bold key phrases and favicon citation clusters | **continuous upward scroll** plus slight zoom-in | Text scrolls ~25% frame per frame | A citation popover appears |
| #70–77 | 4.0 | Citation popover + side caption | Popover "Skin Barrier: High-impact…" plus "Reasoning HIGH CONFIDENCE" panel; the cursor hovers; side caption "Thousands of sources" → "cited and traceable"; then a line chart "Scalp Care Search Interest Over Time" | slight drift left | The caption **types in at the right of the UI** in medium grotesk (~4% height), replaced in place. The chart line draws left→right over 2 frames (#75→77) | Cut to dot-grid card |
| #78–84 | 3.5 | Dot-grid type card | "Data" → "Data changes" → "Data changes fast" → "Your research" → "Your research should too" | red dots drift across the grid | Word append. Red dots reposition every frame (random walk), with a slow push-in | Cut to answer macro |
| #85–90 | 3.0 | Answer macro → isolate | Answer paragraphs; the sentence "Skin barrier repair is moving from niche concern to mainstream expectation" highlighted | push-in | **Everything except the highlighted sentence fades out** (#87–88), leaving the line alone with the Track icon above (#89) | Cursor clicks Track |
| #91–96 | 3.0 | Track button → tracker card | "Track" pill pressed (it fills coral, #92); becomes the "Skin Barrier tracker" card; "Monthly" frequency chip slides in from the right | macro follows | The button press scales ~0.95 and fills. The card expands horizontally from the button. The frequency chip enters from the right edge in its own grey panel | Zoom-out |
| #97–103 | 3.5 | Trackers list | Empty list → the new tracker lands → 4 more trackers stack in → scroll | **zoom out** from 3× to 1.2×, then scroll up | Rows cascade in (#100: 4 rows in 1 frame after the first) | Scroll into the report cards |
| #104–108 | 2.5 | Report cards | A grid of editorial thumbnails with headlines; one card ("Skin Barrier: The Gap Major Brands Aren't Filling") scales to foreground | **tilted/perspective-skewed** (#106–108 cards slant ~5°) with fast scroll | Hero card scales up ~1.6× out of the grid | Cut to type |
| #109–114 | 3.0 | Paper type | "Always on, so you don't have to be" | static | Word append. The "o" of "on" is a coral dot (#110). At #113 the text fades to 20% and the dot grows | Only the dot remains |
| #114–118 | 2.5 | Dot → alert icon | The dot grows into a broadcast icon with 3 huge concentric arcs pulsing (#115), then shrinks to a small icon (#116) that becomes the "New Alert" pill | scale 1→20→1 | Rings expand past the frame edge, then collapse. The pill label blurs in (#117) | "Skin Barrier Tracker" chip slides out beside it (#119) |
| #121–124 | 2.0 | Alert card | "20 minutes ago · Skin Barrier DTC Brand Launches…" card; "3 files" | zoom into the "3 files" button (#123) | Cursor clicks | Files fan out |
| #125–133 | 4.5 | File exports | DOCX / PPTX / XLSX rows on a grey BG; each opens into a document preview | **horizontal pan** left→right across the three documents | The rows stagger-slide (#127 each offset ~20 px further right). Each file expands into a preview page (report cover, slide deck, spreadsheet) | Cut to Slack |
| #134–148 | 7.5 | Slack thread | "#strategy" — Adam asks; Sophie types "Funny you mention it, I just pulled this out of Merciv" and attaches the 3 files | zoom in to macro (#136–141), then out (#146) | Typewriter reply. **Drag-and-drop:** the files fly into the composer (#143). The message is sent and re-rendered as a posted message (#146–148) | Cut to photo grid |
| #149–153 | 2.5 | Photo grid | 3×5 grid of product and beauty photos | static | Photos **removed in random order**, 3–4 per frame, until one remains (#153) | Last photo vanishes |
| #154–161 | 4.0 | Logo end card | The logomark alone, then "Merciv", then "Get started for free at merciv.com" | static | Logomark first (#154), wordmark (#155), URL fades in (#156), hold 3 s | End |

## 4. Transition inventory
- **Photo-under-text swap** (#7–10): the text stays put while the image plate swaps each 0.5 s. A riffle cut.
- **Edge-in collage fill → isolate hero** (#14→19): additive build, then subtractive reveal of one frame.
- **Tiny type → giant type hard cut** (#20→21): a scale-contrast jump of ~15×. The punchline "harder" hits via scale alone.
- **Type stack auto-fit zoom-out** (#21–24).
- **Text collapses into dot → dot becomes logomark** (#24→28): a punctuation-mark morph, then a BG flood.
- **Zoom-cut into macro UI** (#36→37) and **caret-follow track** (#37–47).
- **Prompt → pill collapse** (#50→51): the input box shrinks to the query bubble (a morph).
- **Pull-back reveal** (#64→65): from the source counter out to the query plus answer.
- **Fade-everything-but-one-sentence** (#86→89): an isolation reveal that turns a sentence into an object.
- **Button → card expansion** (#92→93).
- **Dot → icon → rings → pill** (#113→117): a single coral dot carries across three states.
- **Document fan & pan** (#125–133); **drag-into-composer** (#143).
- **Subtractive grid dissolve** (#149→153) → logo on white.

## 5. Easy-to-miss details
- **Three blank frames open the film** (#1–3, 1.5 s of paper). Silence before the first word.
- The interstitial text is **tiny (~1.5% height)**. That makes the jump to 25% "keeping" feel like a shout.
- #23–24: the stacked words are centred and the line spacing is tight (~0.9 leading). The block keeps a constant visual width, shrinking to fit.
- #25→26: the dot travels *leftwards*. It is the period of the sentence exiting to where the logomark will sit.
- #28–30: the logomark bars are dotted/segmented, echoing the background dot grid.
- #37–47: the caret-follow camera keeps the caret around 60–70% of frame width, so text continuously spills off the left edge. The auto-token "Skincare" colour changes mid-type (#40: "Skinca" black + "re" teal, then the whole word gets its chip).
- #42: when "/" is typed, a menu ghost (empty rounded rect) appears one frame before its items fill in (#43). A two-step menu reveal.
- #56–63: the step label **scrambles/erodes letters** as it changes ("We  Search", "Kr  ledge Search", "…ge Se  h"). It's a letter-dropout transition, not a crossfade. Favicon stacks change per step (Reddit → TikTok → YouTube → Target/Walmart).
- The source count ticks non-linearly: 9 → 84 → 305 → 737 → 930 → 1009 → 1028 (ease-out toward the total). Then "1782 considered" slides in to its left.
- #71–74: the right-side caption sits **outside the UI plane** at 2× the UI type size. It's the narrator voice as type.
- #75–77: the chart line draws over ~2 frames. The y-axis gridlines were already present, so only the path animates.
- #78–84: red dots jump position every frame (not smoothly). A deliberately stepped "data flicker".
- #92: the Track press fills the pill coral with white text, a one-frame state change. The cursor is the macOS pointing hand, drawn at ~3% frame height.
- #106–108: the report cards have a slight perspective skew and a motion-blurred scroll. It's the one moment of 3D in the film, used for "volume of output".
- #115: the concentric rings are pale coral (~15% opacity) and much bigger than the frame (outer ring radius ~0.7 frame width).
- #127: the three file rows offset diagonally (stagger ~20 px) as they move, then re-align.
- #143: the files dragged into Slack stack as a pile under the cursor (DOCX on top, others peeking) before landing as three chips in the composer (#144).
- #149–153: the grid dissolve removes tiles in a scattered order. The last surviving tile (hair swirl) sits near centre and gets removed just before the logomark appears on the same spot.

## 6. Pacing curve
Slow, quiet open (1.5 s of nothing, then tiny words) → photo riffle quickens → collage burst (#16–17, busiest frame) → silence → **giant type shout** (#21–24) → the dot morph gives a calm brand beat → **typing sequence at conversational speed** (5.5 s, the longest single action) → source counter speeds up (7 values in 5 s) → answer scrolls fast → breath on "Data changes fast" → isolate → track → tracker list cascade (medium) → a second breath "Always on…" → **ring pulse** (the visual climax, single icon filling the frame) → payoff chain (alert → files → Slack) runs at a steady ~2 s per beat → subtractive grid → 4 s logo hold. There are two type "breaths" dividing three product acts.

## 7. What makes it premium
- Everything happens in **macro**. The viewer never sees a whole screen except once (#32). This reads as editorial, not "screen recording".
- A single query follows through the whole story: question → sources → answer → tracker → alert → deliverables → Slack. The demo *is* the plot.
- Scale contrast in type (1.5% vs 25% height) creates drama without motion tricks.
- A single graphic atom (the dot) links punctuation, logomark, data points, the "o" and the alert icon.
- Real micro-UI states (auto-token chips, slash menu, "Thinking", letter-scramble step labels, button fill) are recreated at slow, legible speed.
- The editorial beauty photography sets taste before any UI appears.

## 8. Reusable techniques
1. **Caret-follow macro typing.** Render the input at ~3× and lock the camera x to the caret, offset 65% of frame width. 6–8 chars per 0.5 s. Tokens (entities) change colour and chip-ify 1–2 frames after the word completes.
2. **Letter-dropout label swap.** When a status label changes, remove 30–50% of letters randomly over 1 frame, then fill in the new label. Pair it with a ticking counter that eases out toward the final number.
3. **Isolate-the-sentence.** On a dense answer, fade all text except the target sentence to 0 over ~1 s, keeping the highlight. Then scale the survivor slightly and bring the action button in above it.
4. **Stack-and-shrink headline.** Add a word per beat below the previous one. Auto-scale the block so the total height stays constant (first word 25% of frame height → last line 8%). Centre-aligned, tight leading.
5. **Punctuation-to-logo morph.** The final period of the headline becomes a dot. Slide it to the logo position (0.5 s), flood the background, then grow logomark bars out of the dot. Type the wordmark letter-by-letter.
6. **Dot → pulse → pill.** A brand-colour dot grows into an icon, emits 2–3 concentric rings larger than the frame (0.5 s), collapses back, and the icon docks into a UI pill with the label blurring in.
7. **Additive collage → subtractive reveal.** Pop photos in from the edges (1→3→8→full within 1.5 s), then delete all but the hero in one frame. At the end, reverse it: a full grid loses 3–4 tiles per frame until the logo spot is empty.
8. **Deliverable chain.** Alert card → "3 files" button → rows stagger out → horizontal pan across previews → drag into chat composer → sent message. Each hop takes about 1.5–2.5 s and carries the same object forward.
