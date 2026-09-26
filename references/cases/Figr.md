# Figr — analysis (82 frames, ≈41 s)

## 1. One-line concept
Figr is an AI virtual try-on / "fitting room" for fashion e-commerce. The spine is a rhetorical question ("What if shopping online felt as personal as stepping into a store?") answered by a single continuous chain of objects: the word "store" becomes a product card, the card's try-on button becomes the app, the app captures you, generates you, and dresses you. Then it closes on a tagline and the logo.

## 2. Visual world
- **Background:** very pale pink base (~#F8E6F0) with huge out-of-focus gradient blobs, like a mesh gradient blurred to roughly 300–400 px at 1920. There are three palettes, one per act. Act 1 (#2–#14) is cool lavender/periwinkle/dusty rose. Act 2 (#19–#25, #62–#82) is warm peach/coral/magenta/yellow. The product demos (#31–#48) sit on a flat pale pink, and #49–#61 on a flat lavender (~#B49CC8). The blobs drift slowly in every hold, so the background never freezes.
- **Halftone dot particles:** in #19–#25 small white dot-matrix clusters sit on top of the warm gradient, scattered around the product. It's a subtle "AI/generation" texture, used only in the scene where the product first transforms.
- **Type:** a humanist/geometric sans, light-regular weight, very small. Copy lines are about 20–25% of frame width and cap height is about 1.5% of frame height, so the type whispers. White on the gradients in acts 1–2. It flips to dark plum (~#4A1F3A) at #71 for the payoff lines. The logo (#79) is a heavy rounded wordmark in dark plum, about 3× the tagline size.
- **UI staging:** real product UI sits on **frameless white phone cards**: rounded rectangles with a status bar but no bezel and a very soft shadow (#22–#25, #31–#40, #67–#70). The Reformation mobile page (#59–#61) is also frameless. Photos are e-commerce cut-outs on white, never lifestyle.
- **Motifs:** the small square figr "try-on" icon button, oval face/body capture guides, measurement callouts in tiny mono caps.

## 3. Shot list
| Frames | ≈s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1 | 0.5 | Empty | pale pink | — | — | blob fades in |
| #2–#4 | 1.5 | Type card | "What if shopping online" center | locked | text blur-in (#2 faint/soft → #3 crisp); lavender blob grows in saturation | line swap in place |
| #5–#7 | 1.5 | Type card | "felt as personal" | locked | text replaces previous at same center; blobs drift | line swap |
| #8–#10 | 1.5 | Type card | "as stepping into a [store]?" | locked | "store" sits in a white rounded highlight box that grows from translucent (#8) to opaque and slightly larger (#10) | the box becomes the card |
| #11–#14 | 2 | Object reveal | product card (model in black outfit, "Harriet High Rise Relaxed Straight Jeans $178") | slow push | card appears small (~15% frame width) with a blurred photo, sharpens, scales ~1.0→1.5 over 4 frames | push-in cut |
| #15–#16 | 1 | Macro crop | crop of the card: jeans, title, bag icon, figr button bottom-right of the photo | continued push (~3–4× total) | the try-on button fades into its square in #15 and is crisp in #16 | the button isolates |
| #17–#18 | 1 | Icon hold | the button alone on a pink-orange gradient tile (~15% frame width) on flat pink | locked | card context gone; tile carries a warm gradient that foreshadows act 2 | the tile expands |
| #19–#21 | 1.5 | Transform | white square with a full-body model photo; background switches to warm gradient + halftone dots | locked | square grows ~80→87 px (cell scale) and nudges left in #21 | morphs to phone |
| #22–#25 | 2 | UI hold | frameless phone "Fitting Room" UI (model, color swatches, size chips) | locked | micro drift; #25 slightly faded/softer | dissolve to type |
| #26–#30 | 2.5 | Type card | "Every shopper becomes themselves inside your store" | locked | text fades up from ~10% opacity (#26); magenta blob blooms upper-left and grows through #30 | cut |
| #31–#35 | 2.5 | UI demo | phone camera capture: oval guide over live feed (sofa → window → woman's face) | locked | feed content moves (simulated handheld pan) while the frame stays static | second phone enters |
| #36–#40 | 2.5 | Split UI | face capture + full-body outdoor capture side by side | very slow pull-out (~3% over 5 frames) | right phone slides in from the right as the left shifts left | cut |
| #41 | 0.5 | Diagram | tiny label top-left, empty outline rectangle | — | frame drawn first | figure fills it |
| #42–#47 | 3 | Diagram build | model cut-out inside the frame, "GENERATION" label, CHEST/WAIST/HIP ticks on the left, measurement list on the right | locked | right-side list adds ~1 line per frame (CHEST CIRCUMFERENCE → … → TROUSER LENGTH); feet fade out with a gradient mask | bg tint darkens (#48) |
| #48 | 0.5 | Color transition | same diagram, bg shifts pink → mauve | — | background color tween | cut |
| #49–#51 | 1.5 | Collage | 3 outfit cut-outs in a triangle on lavender | slight push | photos spread apart and scale ~5–8% | collapse |
| #52–#55 | 2 | Widget | "Fitting Room ^ / 3 IN QUEUE" mini widget with stacked thumbnails | locked | the 3 photos collapse into the widget; gentle float ±5 px | zoom-in cut |
| #56–#58 | 1.5 | Macro UI | expanded fitting-room list (Rory Silk Dress, Cove Cashmere…, Monica Silk Top…) | huge crop, slow pull back | right half of the rows carries a soft blur/shimmer (loading/generation state) | scale-out |
| #59–#61 | 1.5 | Context | full frameless phone: Reformation store page with fitting-room panel | pull back ~2× (#58→#59), then keeps shrinking (#60) | #61 phone sinks under a lavender overlay (fade) | dissolve to warm gradient |
| #62–#66 | 2.5 | Type card | "Forget size charts. The right size finds you." | locked | per-word blur-in (#63 "size" still blurred/offset); warm gradient saturates; #66 the line blurs and drifts left while fading | UI fades over |
| #67–#70 | 2 | UI rapid swap | frameless fitting-room phone, semi-transparent → opaque | slow push (~20% over 4 frames) | the outfit changes every frame (jeans → burgundy top → white dress) | fade to type |
| #71–#74 | 2 | Tagline | "Online shopping just became personal, finally." in dark plum | locked | "finally." blur-in with ~10 px downward offset (#72), settles #73 | line swap |
| #75–#78 | 2 | Tagline 2 | "Invite-only brands" | locked | hold | swap to logo |
| #79–#82 | 2 | Logo | figr wordmark, dark plum, center | locked | background blobs keep drifting | end |

## 4. Transition inventory
1. **Line swap in place** (#4→#5, #7→#8, #74→#75): old line out, new line in at the same centroid. Motivated by one continuous sentence split across cards.
2. **Highlight-box → object morph** (#10→#11): the white box behind "store" grows into the product card. This is the thesis transition: the *word* store becomes a *literal* store item.
3. **Push-in to macro** (#14→#15): continuous zoom into the card until only the try-on button matters. Motivated by directing the eye to the CTA.
4. **Isolate + re-skin** (#16→#17): the button detaches, context disappears, and the button gets a new gradient tile, like an app icon.
5. **Tile → content → device morph** (#18→#19→#22): square → product photo → phone UI. The shape grows while the aspect changes from square to portrait.
6. **Soft dissolve through blob** (#25→#26, #61→#62, #66→#67): UI fades while the gradient blooms. The background carries the handoff.
7. **Slide-in companion** (#35→#36): a second phone enters, doubling the idea (face + body).
8. **Background color tween** (#47→#48→#49): pink → mauve → lavender marks the chapter change without a cut.
9. **Collapse into widget** (#51→#52): three photos gather into the "3 IN QUEUE" stack, showing "multiple jobs become one queue."
10. **Macro-to-context pull-back** (#58→#59): from list rows out to the full store page.

## 5. Easy-to-miss details
- The copy cadence is metronomic: every act-1 line holds exactly 3 frames (1.5 s).
- Text never snaps. Every line is a blur-in (≈8–12 px blur → 0 over ~0.5 s). The last word of a sentence arrives later and lower (#63 "size", #72 "finally.") as a delayed-tail reveal.
- The "store" box starts at ~40% opacity (#8) and ends opaque and larger (#10), so it is already "becoming something" before the morph.
- In #11 the product photo inside the card is blurred and sharpens by #12, a focus-pull on a 2D element.
- In #15 the try-on button's icon is missing; it pops into the white square by #16, a staged reveal of the key UI affordance.
- In #17 the gradient on the icon tile is the *next* scene's palette, a foreshadowing color bridge.
- The halftone dot clusters appear only during the "magic" transform (#19–#25), which marks "AI happening" without a sparkle cliché.
- In the camera capture (#31–#35) the phone stays still but the viewfinder content moves, which sells a live camera cheaply.
- Measurement callouts (#43–#47) stagger one per frame. The figure's feet dissolve into the bg (gradient mask), so the cut-out never has a hard bottom edge.
- Loading state in #56–#58: a blur wash over the right half of rows, not a skeleton loader, which reads as "generating."
- The type color flip white → plum at #71 marks the switch from story to brand statement.

## 6. Pacing curve
Slow, breathy open (4.5 s of type on blobs) → quick object-chain acceleration (#10–#22, a new state every 0.5–1 s) → breather type card (#26–#30) → mid-tempo demo (capture, generation, queue: 1.5–3 s per beat) → second breather (#62–#66) → fastest moment: outfit swaps every frame (#67–#70) as a mini-climax → two calm tagline cards → a 2 s logo hold. The film alternates between type-on-gradient "breaths" and demo "inhales" about every 8–10 s.

## 7. What makes it premium
- One unbroken object lineage (word → box → card → button → tile → photo → phone). The viewer never loses the thread, and the product is *derived* from the copy.
- Tiny type with a huge atmospheric background: confidence through whitespace, not headline size.
- Chapter coding by background palette (cool → flat pink → lavender → warm) instead of title cards.
- UI shown frameless, so the product feels like fashion editorial, not a phone ad.
- AI moments shown by texture (halftone dots, blur-wash loading) rather than glowing particles or "AI" labels.

## 8. Reusable techniques
1. **Keyword box → hero object.** Wrap the key noun in a rounded fill box (fade 40%→100% over 1 s, grow ~10%). On the next beat, scale the box as the container of the product card (0.4 s ease-out, cubic-bezier(0.2,0.8,0.2,1)) and fade the line out.
2. **Push-to-affordance.** From card view, push 3–4× over ~1 s onto the one CTA. Then cut context away and re-seat the CTA on a new tile in the next scene's palette.
3. **Blur-in word tail.** Reveal the line at once but hold back the final word. Bring it in 0.3–0.5 s later with 10 px blur + 8–12 px downward offset → 0 (ease-out).
4. **Palette-per-act backgrounds.** A 3-blob mesh gradient, blurred ~20% of frame width, drifting 2–4%/s. Change hue family at chapter boundaries through a 0.5 s flat-color tween.
5. **Static device, moving viewfinder.** Keep the phone card locked. Pan or zoom only the content inside the camera mask to fake live capture.
6. **Staggered spec list.** Add measurement labels one per 0.5 s beside a cut-out figure with a gradient-masked base.
7. **Collapse-to-queue.** N items converge and scale into a small widget with a count badge (0.4 s). Then hard zoom into the widget to show its contents.
8. **Rapid variant flip.** 3–4 outfit/state swaps at 2 per second on a slowly pushing UI card as the climax beat.
