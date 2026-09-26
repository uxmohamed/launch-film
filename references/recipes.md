# Recipes

Each recipe covers:
- **Structure:** the beats, with timings, assuming 1920×1080.
- **Camera**
- **Elements**
- **Transition logic in and out**
- **Why it works**
- **Refs:** films in `cases/` that use it.

Easing names come from `numbers.md`: `out` = expo-out cubic-bezier(.16,1,.3,1), `io` = cubic-bezier(.65,0,.35,1), `in` = cubic-bezier(.55,0,1,.45), `back` = cubic-bezier(.34,1.56,.64,1).

---

## R1. Introducing the product (the cold open)

**Structure (6–10 s)**
| t | Beat |
|---|---|
| 0–1.0 | Empty ground plate with ambient life only (drifting blobs, grain, a faint grid). Silence is part of the open. |
| 1.0–3.5 | The problem or question sentence, word-append at 0.3–0.5 s per word, with the film's arrival state. |
| 3.5–5.0 | The key noun is emphasised (keyword box fades 40→100%, or an accent colour, or an inverted block), and the sentence re-centres on it. |
| 5.0–6.0 | **The key noun becomes the first product object** (a box → card morph, a phrase → UI field, or a pill that the camera zooms through). |
| 6.0+ | The product world begins. The logo either lands here, in a long film (reveal at 20–35% of the runtime), or is saved for the end in a short teaser. |

- **Camera:** locked, with a slow push (+3% over the sentence). The first move is the push into the key noun (3–4×, 1 s, `io`).
- **Elements:** tiny centred type (1.5–3% of frame height). No UI until the morph.
- **Transition logic:** the product is *derived* from the copy. It grows out of a word the viewer has just read.
- **Why it works:** the viewer reads a claim, then instantly sees the claim become tangible. There's no "here's our logo" pause.
- **Variant, "light through letters":** the title is a dark emboss on black, then a gradient light sweeps through the glyphs and floods the background (0.5 s) (Lovable).
- **Variant, "data spotlight":** a screen of code at 12–15% opacity with one line at 100%. Hold 2 s, then dolly out 1.0→0.5 over 3 s (Adaline).
- **Variant, "UI bar as title stage":** start on the real input bar at ~15% of frame width, push in 4× over 1.5 s, and type the headline *into* it (Aside).
- **Refs:** Figr #1–11, Cosmos, Aside #1–9, Merciv #1–28, Lovable #1.

---

## R2. Revealing a new feature

**Structure (5–8 s)**
| t | Beat |
|---|---|
| 0–1.5 | The feature's clause of the sentence, type on ground (2–5 words). |
| 1.5–2.0 | The clause's last word (or the atom) carries into a floating component card at 25–40% of frame width. |
| 2.0–5.0 | 3–4 micro-states of the followed object, 0.8–1.2 s each. Each is triggered by a cursor, caret or the previous state. |
| 5.0–6.0 | **Payoff:** the one extreme move (a pull-back showing it in context, a ring pulse, or rapid variant flips at 2/s). |
| 6.0–7.0 | Exhale: the card dims to 40% or blur-melts, and the next clause begins. |

- **Camera:** starts close (macro, 2×), drifts toward the action, and pulls back 2–3× in 0.5 s at the payoff.
- **Elements:**
  - Sibling UI elements stagger at 0.4–0.5 s.
  - Neighbours dim to 50% while the active item works.
  - Loading is texture (a shimmer sweep, a blur wash), never a spinner.
- **Transition logic:** in from the sentence; out through dimming, or through the followed object moving to the next step.
- **Why it works:** a feature is framed as a moment in the object's life with a visible cause. The payoff is the only loud moment, so it lands.
- **Refs:** Merciv tracker/alert, Figr capture → generation, Veryfront wizard.

---

## R3. Full product view → specific UI detail

**Structure (3–5 s)**
| t | Beat |
|---|---|
| 0–1.5 | Orientation wide: the full window at 70–80% of frame width on the ground, soft shadow, +5% drift. The target region is subtly pre-lit (hover state, cursor nearby, or the other regions 10% dimmer). |
| 1.5–2.5 | Push 2.5–4× on the target (`io`, ~1 s). The other regions blur 6–10 px or fall off frame. |
| 2.5–3.0 | **Isolate:** the surrounding chrome fades out (0.3 s). The component now floats alone on the ground. Its type is swapped to a film-size version (3–5% of frame height). |
| 3.0+ | Work in macro: follow the caret or cursor. |

- **Camera:** one continuous push. No cut between wide and macro.
- **Detail:** the camera's destination is decided by the *next* action (the button that will be clicked), not by the component's geometric centre. Aim slightly ahead of it.
- **Alternative, grid-cell dive:** if the ground is a grid, push ~2× into one cell (0.8 s) and let the cell *contain* the detail. Repeat per step (Firecrawl).
- **Alternative, scene → card inverse:** shrink the wide scene to a card at 45–50% of frame width and show the detail beside it.
- **Why it works:** the viewer gets context for 1.5 s, then the camera does the looking for them. Isolation turns a crowded screen into a single idea.
- **Refs:** Figr #11–17, Layo #30–31, #47–48, Merciv #36–37, Harvey #106–107 (reverse).

---

## R4. Showing an interaction

**Structure (2–4 s per interaction)**
| t | Beat |
|---|---|
| 0 | The cursor is already moving (it enters from off-frame or drifts in, 20–40 px). It never starts from rest in the centre. |
| 0–0.6 | The cursor travels along a slight arc (ease-in-out). The hover state appears **one frame before arrival**, and the hover band trails the cursor by one frame. |
| 0.6–0.8 | Press: the button scales to 95% and fills with the accent, with an optional sheen sweep (0.3 s). |
| 0.8–1.5 | **Consequence:** the result grows *from* the click point, or a click bloom floods from the cursor's direction of travel, or the container's body swaps in place. |
| 1.5–3.0 | Hold on the result with drift. The cursor keeps drifting slowly, not parked. |

- **Camera:** it may push 5–10% toward the click during the press. For the single most important click of the film, go to a 6–8× macro so the cursor and button fill the frame, then snap back.
- **Cursor design:** give it a character (a labelled multiplayer pill, a brand-coloured oversize bevel, an avatar, or a mobile tap dot). Two different cursors can stand for AI and human (orange "Agent" and blue "Alex").
- **Typing:**
  - 6–8 characters per 0.5 s when the text must be read;
  - 40–60 characters per 0.5 s for texture;
  - one 1 s hesitation for drama;
  - tokens turn into chips 1–2 frames after the word completes.
- **Why it works:** cause → effect is legible, and the one-frame lead and lag mimic a real UI's responsiveness while running at film speed.
- **Refs:** Conduit cursors, Veryfront hero cursor, Layo Publish press, Merciv Track press, Harvey #40–42.

---

## R5. Showing multiple features rapidly

Choose one of these **four patterns**. Don't mix them in one passage.

1. **Slot reel.** A fixed sentence with one word rolling vertically ("can do ___"). Roll every 0.8–1 s; the neighbours sit at 25–40% opacity with vertical motion blur. Optionally, each swap adds one element to a diagram beside it (accumulation). (Aside, Lovable, Adaline)
2. **Fixed-layout slideshow.** An identical composition (image on top, 2-line caption below), hard-cut every 0.5 s. Caption values blur in while labels stay static. (Cosmos #16–19)
3. **Canvas vignettes.** One continuous canvas, 1–1.5 s per vignette, with the camera following a connector. Each vignette uses its own sub-colour, and the icon count doubles per beat (1→2→4) to show scale without words. (Cloudflare #59–68)
4. **Centred-anchor cuts.** Hard cuts every 1–2 s between very different visuals, with a single anchor fixed at centre. (Harvey)

- **Rules:**
  - Nothing to read beyond 1–3 words per item.
  - End the passage on a breath (2 s type on ground) or on the payoff item held longer.
  - The rhythm accelerates slightly through the passage: the first item is held about 1.3× longer than the rest.
- **Why it works:** the viewer feels breadth without processing each feature. The fixed container keeps the eye still while the content changes.

---

## R6. Moving between different parts of the interface

**Choose by relationship:**
- **Sequential steps in one flow:** a one-take along a rail, or a line-follow. The camera trucks at a constant ~120 px/s, a leading dot runs ~100 px ahead, and cards append on the rail. (Aside #74–92)
- **Siblings (tabs, sections):** a sticky-active chapter menu. A left column lists three verbs: active one dark, the others at 20% grey. On a change, scroll the list so the new active line lands at the old one's y position (0.4 s `io`), and swap the right panel and background glow hue *on the same frame*. (Layo, Conduit Reply/Research/Memorize)
- **Nested levels (drill-down):** grid-cell dive, or scene → card shrink.
- **Distant areas:** don't pan across empty UI. Pull back to a wide shot (2–3×, 0.5 s), then push into the new area. Or carry the object: drag a file or chip from area A to area B, with the camera following the object.

- **Why it works:** the transition matches the navigation model, so the viewer learns the product's structure for free.
- **Refs:** Layo #30–47, Conduit #76–114, Merciv #125–144 (deliverable chain: alert → files → pan previews → drag into Slack).

---

## R7. Before / after transformation

**Pattern A: animate the verb (preferred)**
| t | Beat |
|---|---|
| 0–1.0 | The "before" object sits in the context, which dims to 50%. |
| 1.0–1.8 | **The verb sweeps across it:** a dither band, scanner bar, glyph scramble front or re-bin (0.6–0.8 s). The "after" is revealed behind the leading edge. |
| 1.8–3.0 | Hold on the result. The context returns to 100%, and a number or tag confirms it (the tag stagger at 0.5 s). |

**Pattern B: same framing, twice**
- Show the failing "before" in exactly the framing, crop and prompt that the "after" will use later. Separate them by the product sequence that explains the fix.
- The return to that framing *is* the payoff (Layo: the same iPhone crop and the same prompt, first "Sorry, I can't help", then a live map app).

**Pattern C: card slide-over**
- The "without" scene shrinks to a card at 45–50% of frame width, and a contrasting "with" card slides over it from the right. The colours encode the two states: pale for without, saturated for with (Cloudflare "localhost → global").

- **Why it works:** A shows the product *doing* its work. B makes the viewer remember the pain and then resolves it. C makes the argument in a single composition.
- **Refs:** Firecrawl #56/#77/#110, Raindrop scanner, Layo #13/#54, Cloudflare #77–78.

---

## R8. Turning a static dashboard into a cinematic shot

**Structure (4–6 s)**
1. **Never open on the whole dashboard.** Open macro at 3× on one label or number *mid-state* (mid-typing, or the counter still ticking).
2. **Pull back 2–3× in 0.5 s** (`out`) to reveal the chart, while the numbers tick to their final values (3–7 decelerating steps over ~1 s) and the chart line draws. The gridlines are already there; only the data path animates.
3. **Emphasis by luminance:** the brand's bar or line is the only solid or bright element. The others are grey outlines.
4. **Add depth** only if you need to show volume: tilt the dashboard plane ~8° with a slight barrel curve, and give the cards a motion-blurred scroll.
5. **Deconstruct:** lift 2–4 key cards off the dashboard onto the ground plate (a 5–10% scale-up, shadows increasing), and let the rest blur 8 px and dim.
6. **Life:** matrix opacity shimmer, a live-looking ticker that fluctuates slightly, the cursor hovering a data point with a tooltip that trails by one frame.

- **Camera:** a pull-back → hold drift (+3%) → push to one card.
- **Why it works:** a dashboard becomes a reveal with a sequence (detail → context → emphasis) instead of a wall of data.
- **Refs:** Raindrop #21–25, Cloudflare counters, Merciv #64–77, Conduit stats.

---

## R9. UI ↔ typography transitions

**UI → type**
- **UI label becomes the title card.** Scale a heading from the UI up to headline size as the camera pulls out, or the reverse (Aside #68→73).
- **Statement → header.** The reverse move: a centred claim moves to the top-left and becomes the header of the UI or code that proves it (Raindrop).
- **Isolate the sentence.** Everything in a dense answer fades to 0 over ~1 s except one sentence (with its highlight). The survivor becomes the film's caption (Merciv #86–89).
- **Brand emerges between words.** The final sentence's outer words fade to 20%, and the brand name types into the gap, then collapses to the URL (Aside).

**Type → UI**
- **Text first, container second.** Type the sentence bare, then build the input pill around it (98%→100%, fade 0.4 s) (Layo).
- **Keyword box → card** (Figr).
- **Phrase → control.** A snake_case phrase gains an outline and an eye icon, and clicking masks it to asterisks (Aside).
- **Collapse to pill.** The sentence contracts to its centre and a CTA pill expands from the same point (0.3 s); then zoom through it (Cloudflare).

**Type-over-UI caption.** Captions sit *outside* the UI plane at 2× UI type size, as the narrator (Merciv #71–74). A caption's key noun can sit in a chip styled like the UI's chips (Conduit's "unified inbox").

- **Why it works:** words and interface share one physical space, so the film never switches between "slide mode" and "demo mode".

---

## R10. Ending on a strong product or logo moment

**Structure (5–8 s)**
| t | Beat |
|---|---|
| 0–1.5 | The final clause of the sentence (the payoff line, often in a flipped colour: white → brand ink). |
| 1.5–3.0 | **Subtraction:** remove the world (grid lines fade, collage tiles vanish 3–4 per frame, colour drains to the neutral ground, the texture density drops). The last surviving element sits where the logo will appear. |
| 3.0–3.8 | **Logo arrives from the atom:** the dot grows into the mark, the aperture pinches into the glyph, the letters rise with a 40–50 ms stagger (`out`, ~0.5 s each), the outline writes on, or the wordmark is revealed from behind the mark. |
| 3.8–7.0 | **Hold** 2–5 s. The mark is small (4–5% of frame height). It can dim to ~40% before a URL takes over as the final word. A caret can blink on a 1 s cycle. |
| (7.0–8.5) | Optional: 1.5 s of empty ground, or a blur-out 0→15 px with a fade. |

- **Camera:** locked, with at most a 2–3% push during the hold.
- **Bookend:** repeat an element from the first 3 s (the caret, the gradient keyword, the logo animation reversed so the film loops as a palindrome).
- **Never:** a whoosh slam, a lens flare, a logo scaling up big, an instant cut to black.
- **Why it works:** the calm is a confident statement, and because the logo is *earned* from the film's own atom, it feels like a conclusion rather than a sticker.
- **Refs:** Merciv #149–161, Flashback #86–95, Firecrawl #120–133, Veryfront palindrome, Layo caret bookend, Harvey explode → H.

---

## Extra recipes

### R11. Chapter change
A dot at the end of the last line (or the cursor's click) grows to fill the frame in 4–10 frames (`in`). Its colour is the new act's ground. The new chapter title arrives on top with a slowly rotating 1 px outline motif at 20% opacity. Before the dot starts, dim the whole outgoing composition to 30–40% for ~0.5 s ("breath out"). (Adaline #45, Aside, Veryfront)

### R12. Proof and social proof
One big number at ~8% of frame height, ticking, with a small subtitle. Logos pop in 2–4 per 0.5 s around it and stay; some are deliberately cropped by the frame edge. Change the number with a blur-dissolve while the logo field persists and keeps growing. Three numbers in about 9 s is the maximum. (Conduit #166–178)

### R13. "The AI is thinking"
Use exactly one of these textures:
- a shimmer sweep across the status text (1.5 s, left → right);
- hot text cooling;
- an opacity-shimmer matrix (squares re-randomising between 4–5 tints every 0.25 s);
- halftone dot clusters around the object;
- a blur wash over the region being generated.

Pair it with a step label that changes by letter dropout and a counter easing out. (Veryfront, Firecrawl, Figr, Merciv)

### R14. Integrating a human on camera
Frame the speaker in the left third. Graphics live in the right two-thirds: frosted circles, tags in 3 sizes (for depth), and a thin 3 px arc that draws around the head as a gesture. The lower third exits by sliding 40 px plus a blur, not a cut. Enter and exit the footage through a 60–80% wash of the ground colour, or a blur melt. (Conduit, Adaline)

### R15. Establishing taste or category in 2 seconds
A photo riffle: one centred frame with its image swapped every 0.5 s while the frame scales 1.0→1.6 (`in`). On the last image, push to 3× and blur 0→80 px. The blur becomes the film's gradient ground. (Conduit #1–5)

---

# Recipes added from the full 59-film study

## R16. The caption performs the feature (M1/M2, the most transferable device)

**Structure (3–5 s)**

| t | Beat |
|---|---|
| 0–1.0 | The feature's caption on the ground, e.g. "Isolate any object". Word-append on the 0.5 s pulse. |
| 1.0–1.5 | The cursor drifts in and clicks the *verb* or *object word* in the caption. |
| 1.5–2.5 | **The word undergoes the feature** (see the list below this table). |
| 2.5–4.0 | The same operation is then shown on real content in the UI. The caption dims to 40% or leaves by blur. |

The word undergoes the feature in one of these ways:
- isolate: it's boxed and lifted with a shadow;
- recolour: it changes colour;
- translate: it translates in place;
- control: it's circled in hand-drawn marker;
- redact: a one-frame red flash, then an x-mask wipes left→right.

- **Why it works:** the viewer understands the feature on the words they just read, *before* parsing any UI. The caption becomes the demo canvas.
- **Refs:** Google Pics #40–42, #58–62, #85–88, #151; Island redaction; Reve's self-editing title cards.

## R17. Same subject, many treatments (M2 creative tools)
- **Structure:**
  1. Place the subject (a dog, a chair, a word, the logo) at a fixed centre and scale.
  2. A fixed UI anchor (a mode-switcher pill, a prompt box) sits above or below it.
  3. On each click or hover, the rendering changes every 0.5 s: vector → pixel → layout, or shader 1…8. Run 4–10 variants, then land on the canonical version and hold 2 s.
  4. Between subjects, use a 2–4 s breather on a hero output.
- **Camera:** locked, or a slow +3% push across the whole riffle. The variants change; the camera doesn't.
- **Details:**
  - the ground takes its colour from each variant;
  - the slider or value visibly ticks *with* the change;
  - an effect-pill stack grows (1 → 2 → 3 → 7+) as effects combine.
- **Refs:** Affinity #46–74, Figma Shaders #50–56, #86–96, OpenAI Images, Herman Miller #14–19.

## R18. Brand / identity system tour (M3)
- **Structure:** a chant ("More ___." / "Lighter. Friendlier. Accessible.") at 0.5 s per card, with 3–4 chapters, each a strict duotone pair.
- **Per chapter:**
  1. The chapter word shouts at 35–60% of frame height, trucked if it's wider than the frame.
  2. Then *self-describing* demos: each property is animated by what it names (weight axis for "lighter", a bezier bend for "friendlier", a contrast ramp for "accessible", step-and-repeat for "scalable").
  3. Then the system in context: the mark at a fixed centre, riffled across real placements (billboards, apps, packaging) at 0.5 s.
- **Transitions:**
  - component-as-wipe (the system's own components push the content);
  - polarity flip on the key word;
  - press → iris;
  - palette-stripe wipe.
- **Ending:** an asset wall of every image in the film, pulled back, then cut to a big lone mark (25–45% of frame height) on an emptied ground, held 1–3 s.
- **Refs:** Netflix, Coca-Cola, Uber, Material 3, Walmart, Instagram.

## R19. Model announcement or manifesto with no UI (M4)
**Structure (45–90 s)**

| Phase | Beat |
|---|---|
| 0–25% | **Hidden-subject ladder:** unreadable macro crops of the motif, holds shrinking ×0.8 per shot (4.5 s → 0.5 s). No camera motion. |
| 25–60% | **Found-glyph riffle:** the motif (a version number, a key word) built from 20–40 real materials at 2/s, with an identical centre and scale. Or a diegetic word inventory, or a shape-rhyme chain. |
| 60–70% | **Climax by slowdown:** holds lengthen (2.5 → 4.5 s), then the first camera move of the film, or a black breath before a punchline. |
| 70–80% | **Natural-cause wipe:** a specimen flies at the lens, clouds occlude, or a bird takes off, revealing the title ground. |
| 80–100% | Title and brand (withheld until now), held 5–13 s. Life comes from world elements leaving one by one, or from a slow camera tilt under screen-locked type. Optional: loop to the opening frame. |

- **Annotation option:** hairline "reasoning" lines tracked to real motion in the footage show the AI thinking without UI.
- **Refs:** Claude Fable 5, Fable 5.1, Keep thinking, Index, Apple.

## R20. Hardware benefit costumes (M5)
- **Structure:**
  1. Open on the rim-lit silhouette: the body at ~5% luminance, with a highlight travelling around the bevel for ~3 s.
  2. The product at dead centre; the spec arrives as an **ingredient** (a paper chip lowered into the product, with a 1-frame lightning jolt).
  3. Each benefit grows *out of the body* as a costume. Each costume lasts 2.5–8 s and escalates in complexity, with a 0.5 s reset to the bare product between costumes.
  4. Corner-flush caps label each chapter (a different corner each time) with a micro-text spec margin.
  5. For software on the device, push through the screen (the ground switches diegetically).
  6. End with a material wipe (the world's substance fills the frame), then the logo, held 1–2 s.
- **Refs:** Mac mini, Herman Miller, Perplexity.

## R21. Two-world film (problem world → product world)
- **Act I (~35%):**
  - A hot, textured duotone photo collage, cut every 0.5 s.
  - Questions in the viewer's voice over a soft blob whose hue cycles each question.
  - The anxious key word sits on the blob's brightest area (anxious dropout).
- **Hinge:**
  - The wordmark as 1–2 px outline letters with bezier anchors, trucked across the last problem image (~1 s).
  - It fills with the gradient (0.3 s) and whites out.
  - The wordmark is retyped small inside a construction cell.
- **Act II (~65%):** a white clinical world, hairline construction lines, 1–2.5 s beats, UI and proof.
- **Refs:** Superpower; Affinity's pain montage; Burp's rewind reset (a variant hinge).

## R22. Prompt ritual: teach the core loop by repeating it (M1/M2 with a simple loop)
**Loop (7–10 s), repeated 3–5× with different prompts**
1. Dim the app to ~40% under a white wash.
2. Pull the prompt box forward (85% of frame width, soft shadow).
3. The text types or ghosts in.
4. Push ~3.5× onto the send button, and the cursor clicks.
5. A dark status-pill macro with a colour bloom ("Generating…"). The bloom's colour and position match the next shot's placeholder.
6. Pull back to the placeholder in the output's aspect ratio, and the result resolves.

- **Why it works:** repetition is the point, because the viewer learns the product's rhythm. Vary only the prompt, the output and the bloom colour.
- **Refs:** Google Pics ×5; OpenAI's shape-shifting stage window.

## R23. AI agents as characters
1. Give each agent a coloured pointer and a name flag. Introduce them as floating pixel-art characters around the headline.
2. The same-coloured cursor later performs a real UI action (drags a deal card).
3. A left-column status log appends process verbs at 2 lines/s, with older lines at 40%.
4. The last log line stays put while the words around it change into the next headline.
5. A blank card with a soft glow (~0.5 s) = "generating".

- **Human counterpart:** a separate colour and name (Conduit: orange "Agent" vs. blue "Alex"). The human edit beat shows the user retyping a placeholder in their own words, a trust beat.
- **Refs:** Zaro, Conduit, Cowork.

## R24. Time passing without title cards
- **Overnight:**
  1. Pull back through content → window → a flat illustrated laptop (~1.5× over 2 s).
  2. Warm the screen to sunset and close the lid (~1 s).
  3. The screen glow persists as a dithered "away" ground.
  4. A status pill cycles 3–4 verbs at 1.5–2 s while you're away.
  5. Morning: a phone rises from the bottom edge; the status-bar clock reads 8:14 → 8:19 → 8:21 across shots.
- **Presence-coded grounds:** user present = brand colour; AI working = off-white; user away = halftone.
- **Refs:** Claude Cowork; Burp's stopwatch across a cut; Shapes' clock match-cut riffle.

## R25. Founder documentary open (M6, 90 s+ films)
1. **Historical parable (30–35 s):** 5–6 captioned graphic beats:
   - a date on the grid;
   - a stipple portrait with a name;
   - a map with a dashed route;
   - an instrument with an error readout;
   - a single-jump casualty count, then a 20% scale-up;
   - "N years later".
2. **Match the parable's render style onto the founder:** a stipple dot cloud crossfades to footage (~1 s). The person enters *through the atom*.
3. **Interview home base:** big captions composited behind the speaker's head (12–15% of frame height, alternating sides), a negative-space HUD, and stats with an accumulating logo field.
4. **Testimonial:** a slit-open card with handles, ruler ticks and a live waveform, receding and blurring under a pull-quote.
- **Refs:** Sphinx, Conduit.
