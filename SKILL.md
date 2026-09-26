---
name: launch-film
description: Production manual for product launch films, feature teasers, brand/identity films, model announcements and hardware spots, in the style of top studio launch work (Anthropic, OpenAI, Apple, Netflix, Linear/Arc-tier). It covers concept, mode selection, storyboard, animation and render. Use it when asked to make, plan, storyboard, animate, critique or improve a launch video, announcement film, sizzle reel, brand-system film, or "a video like X's launch", including turning UI screenshots, a product feature or a brand identity into a cinematic motion sequence. Reverse-engineered from a frame-by-frame study of 59 real launch films (see references/cases).
---

# Launch Film: production manual

**Source:** 59 films, 7,495 frames, analysed shot by shot at about 2 fps. Cosmos was also studied at its native 25 fps, which gave the precise easing values. Per-film notes are in `references/cases/`; cross-film comparisons are in `references/cases/crosscut_*.md`.

The goal is to make new films that feel like the same world-class team made them, without copying any single film.

**Read on demand:**
- `references/modes.md`: **read first.** The six film modes and each mode's rule overrides. Most "rules" depend on the mode.
- `references/taxonomy.md`: shot types, transition families, arrival/exit/emphasis states, anchors, annotation layers, with when to use each.
- `references/recipes.md`: 25 step-by-step recipes (intro, feature reveal, full → detail, interaction, rapid features, before/after, dashboard, UI ↔ type, ending, plus mode-specific ones).
- `references/numbers.md`: durations, easing, scale, blur, opacity, type size, by mode.
- `references/implementation.md`: build and render (a deterministic `render(t)` HTML timeline, frame capture, ffmpeg, studying references).
- `references/cases/*.md`: per-film breakdowns. Cite them when you justify a choice.
- `templates/storyboard.md`: fill it in **before** animating.
- `examples/`: a working 20 s film engine (`cadie-film.html`), a renderer (`render.js`) and a contact-sheet slicer.

---

## 1. The design philosophy in one paragraph

A great launch film is **one idea performed, not a list of features explained.** It has a single spine, usually a sentence and sometimes a motif (a word, a glyph, a subject), that the whole runtime spells out, with the product proving each clause. One small brand element (a dot, caret, period, pixel, frame or silhouette) holds the film together: it stays anchored while everything around it changes, or it becomes each next thing. Motion is never decoration. Every change is *caused* (a click, a keystroke, a word, the product's own verb, even a bird taking off), and the transformation itself is shown rather than cut around. Everything runs on a **0.5 s pulse**: about 2 beats per second, so the eye learns the rhythm and the film can be fast without being chaotic. Each film picks a register (whisper or shout, still or moving, sparse or dense), holds it with discipline, and breaks it once where it matters. It ends by clearing the stage for the name.

## 2. Universal laws (held across all 59 films)

1. **One spine.** Write the film as one sentence (6–20 words split across the runtime), or choose one motif that recurs in every shot (Keep thinking: the word PROBLEMS in 13 materials; Fable 5: the digit 5 built from 40 media). Demos, footage and cuts are *clauses* of the spine. Test: stripped of visuals, the spine alone should read as copy or as a single image.
2. **One anchor or atom.** Choose one small brand element and give it one of two jobs, or both:
   - **Carrier:** it becomes the next thing. Merciv's period becomes the logo, the "o" and the alert icon. OpenAI's dot becomes a caret, disc, rings, grid, swatch, mask and logo seed.
   - **Anchor:** it holds position while the world changes around it. Examples: Harvey's centred dot, Opera Air's bubble, OpenAI's spec-sheet frame, Walmart's Spark, Blueprint's grid, Affinity's mode pill.

   It appears in the open, in at least two transitions, and in (or just before) the logo.
3. **A fixed centre makes cuts cohere.** When an element keeps an identical position and size across cuts, hard cuts read as morphs. When it doesn't, the film needs another carrier: object, layout, palette plus tempo, line, or light.
4. **Every boundary has a carrier.** Before animating, name what crosses each scene boundary. Strongest to weakest:
   1. object;
   2. atom;
   3. cause (click, bloom, press → iris);
   4. line;
   5. layout reprise;
   6. anchor;
   7. world or light;
   8. palette plus tempo;
   9. melt.
5. **Chapter coding by ground.** Acts or meanings are marked by background colour, texture or density, never by title cards. Grounds can encode more than acts:
   - argument (t0: cream = ambition, black = problem, green = product);
   - rhetoric (Apple: grey = statement, green = pledge, black = "but");
   - presence (Cowork: blue = the user is here, halftone = the user is away).
6. **Show the verb.** When the product transforms something, animate the transformation itself (a dither sweep, denoise, hot text cooling, a still coming alive, a slider scrubbing, a redaction wiping across the word). A cut from before to after wastes the best moment. The exception is a rhetorical before (the problem montage), which may cut.
7. **Every change is caused.** Clicks, keystrokes, the product's verb, a word's meaning, a UI component's own native motion (a pull-to-refresh spinner dragging the title away) or, in films with no UI, natural motion (a bird taking off, clouds occluding the type).
8. **The newest element has an arrival state,** and the old one an exit. Type never simply appears. Pick an arrival family per film, or one per *meaning* (Opera Air: "focus" blurs into focus while "Create" types). Plan exits too: backspace, blur-scatter, occlusion, shrink-out.
9. **The 0.5 s pulse.**
   - Word appends, slot items, riffle images, stagger steps and cut rhythms all sit on a 0.5 s grid (0.25 s for sub-beats).
   - About 2 words per second is readable when each on-screen fragment is 1–3 words; full lines need 1.5–2.5 s.
   - Variety comes from changing the *mechanism* on the pulse, not the tempo. Apple keeps 0.5 s per word for 97 s by rotating through seven mechanisms.
10. **A register, and one inversion.** Each film commits to a register. Whisper films shout once (Merciv's "harder"). Shouting films whisper once (Apple's "(This is a big one)", Coca-Cola's tiny "timeless."). Still films move once (Fable 5's first camera move after 20 s of stillness). The inversion is the emphasis.
11. **Replace spinners with texture.** "Working" is shown as a shimmer sweep, hot text, a blur-bloom of the input, a glow card, an opacity-shimmer matrix, a status relay, an echo word behind a status pill, dashed rings completing into checks, or a hue-rotating focus stroke. The only exception is when the "generating" glow is itself a colour bridge into the next shot (Google Pics).
12. **Bookend.** The first and last seconds share an element: a caret, a lock-up, the same footage re-captioned, a reversed logo animation, or a palindrome for loops. About three-quarters of the films do this.
13. **End by clearing the stage.** Either subtract (grid off, colour drained, tiles removed) or accumulate everything and then cut to the lone mark. The mark lands on an emptied ground, and nothing slams unless the ground was emptied first.

## 3. Mode-dependent rules (see `modes.md` for the full tables)

| Rule | Product launch / SaaS | Creative tool / generative | Brand / identity system | Manifesto / model / essay | Hardware / physical | Founder documentary |
|---|---|---|---|---|---|---|
| Type size | Whisper, 1.2–3.5% h | Mixed, many faces | Big registers, 7–60% h | Varies; words may be diegetic | Big corner labels, 6% h | Captions 4–15% h |
| Continuity | Object lineage | One subject, many treatments | Palette + tempo + mark | Motif-anchored montage | The product at centre, in costumes | Interview as home base |
| UI staging | Rebuilt, macro, 1–3 full windows | Output *is* the ground; UI pill as anchor | Components as actors and wipes | Little or no UI | Rim-lit silhouettes, ingredient chips | UI as a HUD, captions behind the head |
| Brand reveal | 15–35% of runtime (long films); end (teasers) | Early lock-up + bookend | 0–2 s + end | 67–96% | 90–95% | 35–50% |
| End hold | 2–5 s | 1.5–3 s | 1–3 s, with a big mark (25–45% h) | 2–13 s | 1–2 s | 2–4 s |
| Accent | One, with meaning | Grounds from the artwork; UI accent constant | Strict duotone pairs per chapter | One warm accent | Brand metal/colour | Photo-derived gradients |

## 4. Turning a feature into a sequence

1. **Pick the mode** (`modes.md`). It changes the continuity strategy, the type register and the ending.
2. **State the feature as a before → after of one object** ("a guest message → a booked room"). For creative tools, state it as "one subject → N treatments". For brand films, state it as "one claim → the element demonstrating it".
3. **Find the product's verb** and its visual metaphor (`taxonomy.md` §C "verb transitions"). If the product has a signature UI component, consider making that component the transition (a component-as-wipe).
4. **Write the clause** of the spine that this feature proves (2–6 words).
5. **List 3–5 micro-states** the object goes through in the real product. These are the beats, 1–3 s each, on the 0.5 s grid.
6. **Choose the payoff moment.** It gets the single extreme move: a zoom-through, a 4–5× pull-back, a ring pulse, a variant flip, or a long still hold.
7. **Decide what comes in and what goes out** (the carrier from the previous scene, the carrier to the next).
8. **Consider "the caption does the feature":** click a word in the caption and the word itself undergoes the feature (isolated, recoloured, translated, redacted) before the UI appears. It's the most transferable device in the library.
9. **Add one easy-to-miss detail** (a hover one frame early, the caret turning red before a delete, a letter-dropout label, colour-coded cursors, the clock advancing).

## 5. Plan before animating

Fill in `templates/storyboard.md`. It covers:
- mode;
- spine;
- the followed object or the fixed subject;
- the atom and its jobs;
- ground and act colours;
- type system (register, arrival family, exit family, emphasis method, the one inversion);
- staging rules;
- beat sheet on the 0.5 s grid;
- pacing curve;
- continuity audit (a carrier for every boundary);
- one easy-to-miss detail per scene;
- bookend.

Animate only when the beat sheet reads like a finished film.

## 6. Pacing and rhythm

- **Shape:** a quiet open (0.5–1.5 s of ground or silence, or an unreadable macro) → acceleration → a breath → proof → a density peak or climax → a breath → a clean ending. Inhale (proof, 3–10 s) alternates with exhale (type on ground, 1.5–3 s) about every 8–10 s in product films.
- **Tiers:**
  - pulse: 0.5 s;
  - text beat: 0.5–1.5 s;
  - UI action: 1.5–3 s;
  - reading shot: 2.5–5 s;
  - one-take proof: 6–13 s (up to about 30 s in 100 s films).
- **Speed comes from removing reading.** Riffles carry nothing to read, or carry *the same* one thing in every frame (a found-glyph riffle).
- **A climax can be a slowdown.** Examples: Fable 5's holds grow from 2.5 to 4.5 s; Opera Air's breathing hold; Keep thinking's 2.5 s black breath before the punchline.
- **Hidden-subject ladder.** Open on unreadable macro crops whose holds shrink ×0.8 per shot, so the viewer discovers the pattern.
- **One deliberate hesitation** (a 1 s caret pause), and one rhythmic rupture (a one-frame flash).
- **Front-load or withhold the brand deliberately, by mode.**

## 7. Camera around UI and objects

- The camera is a **reader**: it arrives just before the eye wants to.
- **Moves, calm → loud:**
  - hold drift (±3–5% over 2–3 s; it can also shrink, to anticipate multiplication);
  - push to an affordance (3–4×);
  - caret-follow (the caret held at 60–70% of frame width);
  - line-follow;
  - word truck across oversized type;
  - pull back to context (2–5×);
  - icon-first pull-back (open on the icon, pull back to find it's a toolbar button);
  - zoom-through (10–12×, with motion blur and 1–2% RGB fringe);
  - push through a device screen or an instrument aperture.
- **Anticipate, then land on something.** Every push ends on a glyph, cell or button that starts the next scene.
- **Stillness is a choice.** Lock the camera for text-heavy, wizard or riffle films. Life then comes from the world: typing, props changing state, particles, butterflies leaving.
- **Nest scenes.** Push into a grid cell to reveal the next step, or shrink a scene into a card and slide the next card over it.
- **Aspect ratio and window shape can be the camera** (OpenAI's image window changes 2.35:1 → square → portrait; Keep thinking switches mattes per cut).

## 8. Animating UI so it doesn't feel like a prototype

- **Rebuild your UI** at film type sizes, removing chrome that doesn't matter. **Borrow other companies' UI** when it stands for the problem (Shapes: Gmail and Sheets). **Show real chrome once**, late, as proof (AI Studio, Spellbook).
- **Slow to film speed.** UI beats last 1–2 s, siblings stagger 0.4–0.5 s, and exits may run at UI speed (a one-frame stagger).
- **Show the micro-states:**
  - the hover a frame early;
  - the empty menu before its items;
  - a token turning into a chip after the word completes;
  - a button fill, and a relabel ("Next" → "Complete");
  - the placeholder swap as the thesis ("Ask anything" → "Do anything");
  - a validation appearing after typing stops;
  - a sibling-coupled press (the pressed button widens and its siblings narrow).
- **Typing encodes importance:**
  - 6–8 characters per 0.5 s when it must be read;
  - 15 characters per 0.5 s for a hero prompt;
  - 40–60 characters per 0.5 s as texture.
  - The caret doesn't blink while typing, only when idle. The caret shape or colour can carry meaning (block = terminal era, I-beam = editor; red just before a delete).
- **Text has a lifecycle.** It types in, and it can **backspace out** at 2× speed into the same spot. Editing verbs (select-all, italic toggle, delete) can serve as transitions.
- **Cursors are characters.** Label them (Agent/Alex, Senior Partner), colour them per actor (one colour per AI agent), make them avatars or a plain dot, or use an emoji hand for TV. Keep them drifting. Carry collaborator names across shots.
- **Counters:** process meters (percentage, progress) tick *linearly*. Totals *decelerate* (3–7 steps) or make a single jump plus a 20% scale-up. Real-time tickers run at true speed during holds, as life.

## 9. One continuous narrative

- Use the carrier ranking in §2.4.
- Use thread devices:
  - one project running through every feature (ChatGPT's lamp line);
  - one prompt shown twice, failing then succeeding (Layo);
  - the prompt as table of contents (Cowork: each highlighted clause pays off in order);
  - the vocabulary taught first, then found in the UI (Netflix badges);
  - named cursors that persist between shots.
- Tell time without title cards: a status-bar clock advancing, closing a laptop lid, a stopwatch that keeps running across a cut.
- Two-world films (problem world → product world) hinge on the wordmark: outline letters with bezier anchors fill, then white out.

## 10. Variation within one language

- Keep the **grammar** fixed: ground logic, atom, pulse, type families, arrival family, accent meanings. Vary the **vocabulary** per beat: entrance mechanism, staging, camera move, annotation.
- Rotate mechanisms on the pulse: append → slot reel → backspace-retype → scale shout → decode → caption-performs → morph.
- Use **same subject, many treatments** (a fixed position and scale while the material or style changes), **reprise with a twist** (the same composition with new content), and per-act variants of one motif.
- Annotation layers add a second voice without new grammar: a hand-drawn marker (t0), a proofreader caret (Apple), a pencil underline (Index), a hairline reasoning overlay on footage (Keep thinking), or an arrow-label (Wabi).
- Change one axis at a time between scenes, *unless* type size and position stay fixed. Then ground, colour and wording can all flip at once (Apple).

## 11. Mistakes that look cheap (validated across all 59)

- A feature list or grid with no spine. A slide-style bullet list. (Bullets are acceptable only when styled as the film's own data labels.)
- Raw screen recordings of *your* product. Long, frozen full windows with no project thread.
- Stock transitions that don't come from the product: light leaks, whips for their own sake, cube spins.
  - Glitch or light-burst is acceptable **once**, on the claimed word, and must decay within 2 frames.
- A tilt on wide shots. (Tilt means detail; tilting macros consistently is fine.)
- Literal stock-footage puns (a rocket for "launch"). They were the weakest moments in the set.
- Everything moving at once. Unmotivated drift. A metronome of identical easing and duration.
- Big type everywhere *without* a register (big type as a system is fine; big type as noise is not).
- Accent colour used for decoration. Several accents with no fixed meanings. (Two accents with fixed meanings is fine.)
- Spinners and sparkles as "AI". Lorem ipsum or fake-looking data. Real, specific data sells the film.
- A logo slam on a busy ground. A CTA with no hold. Branding a manifesto in its first second.
- Cutting from before to after when the transformation itself could be animated.

## 12. Production workflow

1. **Brief:** product, launch, audience, runtime (teaser 15–30 s, feature 30–60 s, launch 60–110 s), format, real assets.
2. **Choose the mode.** Read `modes.md`.
3. **Research:** the real UI micro-states, the product's verb, its signature component, and the smallest brand element.
4. **Write the spine.** Iterate until it reads as a poem.
5. **Storyboard** (template). Include the continuity audit.
6. **Build the world first:** ground logic, type styles, atom, card style, annotation layer. Render one still per act and check that they belong to one film.
7. **Rebuild the components** as independently animatable layers.
8. **Blocking pass:** linear motion on the 0.5 s grid, at full speed, with the audio bed. Fix the rhythm here.
9. **Motion pass:** easing families, arrival and exit states, staggers, 30–60% overlaps.
10. **Transition pass:** build every carrier so the boundary frames match exactly.
11. **Life pass:** drift or world motion, cursor micro-motion, shimmer, and one easy-to-miss detail per scene.
12. **Review:** stills at every boundary (±1 frame) and at every beat's midpoint, as a contact sheet. Compare side by side with the closest case in `references/cases`.
13. **QC** (below) → fix → final encode.

## 13. Quality-control checklist

**Per shot**
- [ ] **Story:** it proves a named clause of the spine, and the followed object or fixed subject is present.
- [ ] **Attention:** exactly one place to look. Everything else is dimmed, blurred, small or still.
- [ ] **Readability:** fragments of 1–3 words get at least 0.5 s, and full lines at least 1.5 s, unless the text is deliberately texture.
- [ ] **Continuity:**
  - the carrier in and the carrier out are named;
  - the boundary frames match in position, scale and colour;
  - or a fixed anchor holds.
- [ ] **Cause:** you can say why the frame changes, in the product's or the world's language.
- [ ] **Motion craft:**
  - entrances use expo-out, push-throughs ease-in, and re-centres ease-in-out;
  - properties overlap;
  - there's one delayed secondary element;
  - holds have life (drift, or world motion).
- [ ] **Register:** type size and colour follow the system. The inversion is used at most 1–2 times.
- [ ] **World:** the UI sits in the film's world. A device only when the platform, its state or the owner's product is the point.
- [ ] **Craft signature:** one detail you'd only notice on a second viewing.
- [ ] **Cheapness test:** it would still look designed if the motion were removed, and it never looks like a slide.

**Per film**
- [ ] The spine reads alone.
- [ ] The atom or anchor appears in the open, in at least two transitions, and at the logo.
- [ ] The pulse is audible in the edit.
- [ ] There are 2–3 breaths, one climax (a burst, a pull-back or a stillness), and one hesitation.
- [ ] The brand timing fits the mode.
- [ ] The ending clears the stage and holds for the mode's duration.
- [ ] The bookend matches the open.
