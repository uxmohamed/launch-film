# Taxonomy: shots and transitions

Each entry gives what it is, when to use it, how it's built, and where it appears in the studied films. Timings assume 1920×1080. Frame references (#n) are to the ~2 fps contact sheets in `cases/`.

---

## A. Shot types

### A1. Type on ground (the "exhale")
- **What:** copy only, centred, small (1.5–3.5% of frame height), on the film's ground plate.
- **Use for:** the thesis, chapter statements, breathers between demos, the setup before a payoff.
- **Build:** word-append with the film's arrival state. Hold 1.5–2.5 s after the last word. Add ambient life (drifting background, a 3% push).
- **Seen in:** Cosmos, Adaline, Figr, Layo, Merciv, Cloudflare.

### A2. Scale shout
- **What:** one word or phrase at 25–40% of frame height, right after tiny type.
- **Use:** once per film, on the emotional pivot ("harder", "Track", "You").
- **Build:** a hard cut from tiny type, or an oversize-settle (150–160% → 100% in 0.5–1 s, expo-out). Stack the following words underneath and shrink the block to fit.
- **Seen in:** Merciv #21–24, Raindrop #26, Lovable #8.

### A3. Macro UI
- **What:** the camera is inside the app at 2–4×, showing a single component (input, row, button, label). The frame edge cuts the UI.
- **Use:** any interaction the viewer must read, and the majority of demo time.
- **Build:** a rebuilt component with UI text at 3–5% of frame height. The camera follows the caret, cursor or line.
- **Seen in:** Merciv #37–47, Layo #44–47, Aside, Figr #56–58.

### A4. Orientation wide
- **What:** the full window or page, at 70–80% of frame width, on the ground plate, with a soft shadow.
- **Use:** 1–3 times per film, to tell the viewer where they are before diving in, or as a pull-back payoff.
- **Build:** hold 1.5–5 s with a +5–15% push. Never full-bleed.
- **Seen in:** Harvey #23–27, Figr #59, Layo #26, Merciv #32.

### A5. Floating component card
- **What:** one frameless card (chat, product, sign-in, result) at 25–40% of frame width in generous empty space.
- **Use:** a single state or a result, and as a morph-chain station.
- **Seen in:** Firecrawl (a chat card at 25% width), Veryfront, Figr.

### A6. Deconstructed layout
- **What:** UI chips, pills or cards pulled out of the app and arranged as a diagram: hub-and-spoke, rail, deck, tilted plane or grid.
- **Use:** to explain structure (what connects to what) or volume (many outputs).
- **Variants:**
  - a hub with four chips at compass points (Harvey);
  - a timeline rail with a leading dot (Aside);
  - a Rolodex deck (Firecrawl);
  - a curved plane of dozens of pages (Firecrawl #72–75);
  - an isometric page stack (Flashback).

### A7. Redrawn world
- **What:** the product's output rendered in the film's own language (ASCII, node diagrams with selection handles, dot matrices).
- **Use:** when the product is infrastructure or invisible, or when screenshots would look generic.
- **Seen in:** Raindrop (everything), Cloudflare (architecture canvas).

### A8. Device shot
- **What:** a phone or laptop with a real bezel, usually cropped at 50–60% of its height and rising.
- **Use:** only when the *platform* matters (someone else's app, mobile-native). Frameless otherwise.
- **Seen in:** Layo (ChatGPT in an iPhone), Aside (a MacBook), Cosmos (a bare screen, no bezel).

### A9. Abstract metaphor interlude
- **What:** primitives such as spheres, cubes, rings, domes and pyramids, or collage, standing for a concept (drift, complexity, epochs, chaos → order).
- **Use:** between product acts to reset attention and carry the thesis. Keep each to 1.5–3 s.
- **Seen in:** Adaline orbits, Harvey cubes, Flashback epoch symbols.

### A10. Human in the world
- **What:** a founder or user on camera. They are integrated, not intercut.
- **Build options:**
  - **negative-space HUD:** the speaker in the left third, with graphics in the right two-thirds;
  - **cream wash:** the video appears under a 60–80% overlay of the ground colour;
  - **avatar as cursor:** people shown as data.
- **Seen in:** Conduit, Adaline, Lovable.

### A11. Proof shot
- **What:** a big number (about 8–15% of frame height), an accumulating logo field, or a benchmark bar where the brand's bar is the only solid or bright one.
- **Build:** numbers tick in decelerating steps. Logos pop in 2–4 per 0.5 s and stay. The field only grows.
- **Seen in:** Conduit #166–178, Firecrawl "1,000,000", Raindrop charts.

### A12. Montage riffle
- **What:** an image swapped every 0.5 s in a fixed frame, or a collage filling from the edges.
- **Use:** to establish taste or category in about 2 s. Nothing to read.
- **Seen in:** Conduit #1–4, Merciv #7–19, Flashback's archival montage, Cosmos's caption slideshow.

### A13. End card
- **What:** a small logo (about 4–5% of frame height), a wordmark, or a URL on an emptied ground. Held 2–5 s, optionally followed by 1.5 s of empty ground.

---

## B. Transition types

Grouped by what carries continuity. Each entry gives its motivation, build and duration.

### B1. Object lineage (strongest)
| Name | Build | Duration | Seen in |
|---|---|---|---|
| **Morph chain** | Keep the centre fixed and change the container's size, aspect ratio and contents at each station (box → card → button → tile → photo → phone). | 0.4–0.5 s per station | Figr #10–22, Layo #49–56 |
| **Keyword box → object** | The highlight behind a word fades 40→100% and grows about 10%, then becomes the product card. | ~0.4 s morph (the fade-up takes ~1 s) | Figr #8–11 |
| **Text → UI** | A phrase gains a field outline and icon and becomes the real control (a snake_case phrase becomes a password field). | ~1 s | Aside #153–157 |
| **Prompt → pill → result** | A sent message collapses into a status pill (with shimmer), then splits or expands into the result. | 0.4 s + 1 s | Lovable, Merciv #50→51 |
| **Flat layout → device** | The full-frame layout already matches the in-app layout, so it scales down into the phone screen. | ~0.6 s | Cosmos #20→21 |
| **Collapse to widget** | N items converge into a small widget with a count badge, then the camera zooms into the widget. | 0.4 s | Figr #51–52 |
| **Scene → card** | A deep full-bleed scene shrinks to a bordered card at 45–50% of frame width, and the next element takes the freed space. | ~1 s ease-in-out | Cloudflare #31→32 |

### B2. Brand atom
| Name | Build | Seen in |
|---|---|---|
| **Punctuation → logo** | A headline's period becomes a dot, slides to the logo position (0.5 s), and the mark grows out of it. | Merciv #24–28 |
| **Dot grows into ground** | A dot or circle scales from ~0.3 to >1.5× the frame width in 4–10 frames (ease-in). Its colour is the new act's ground, and text inside cross-fades mid-scale. | Adaline, Aside #106–108, Veryfront #7–9 |
| **Ground → icon** | The inverse: a full-frame colour card contracts as a rounded squircle into the product icon. The next UI grows from under it. | Veryfront #39–40 |
| **Aperture → logomark** | An image window between the halves of a split wordmark narrows exponentially (×0.5 per 0.5 s) while the image inside swaps, then pinches into the glyph. | Flashback #30–33 |
| **Logo as mask** | The wordmark is revealed from behind the logomark's circumference. Reverse it for the ending. | Veryfront |
| **Centred anchor** | A small dot (3–4% of frame) stays at the exact frame centre through 6–10 hard cuts of different geometry, so the cuts read as morphs. | Harvey #65–102 |

### B3. Cause-driven
| Name | Build | Seen in |
|---|---|---|
| **CTA zoom-through** | The pill expands from its centre (0.3 s) and holds 0.5 s. Then an exponential push of ~12× over ~1 s, with directional blur and a 1–2% RGB split at peak speed, lands on a glyph that becomes the first element of the next scene. | Cloudflare #17–26 |
| **Click bloom** | On click, a radial gradient floods the frame from the side the cursor *entered from* (it continues the cursor's direction of travel), in ~0.5 s, landing on the next chapter card. | Veryfront #17–19 |
| **Push to affordance, then isolate** | Push 3–4× onto one button. Remove the context, then re-seat the button alone on a tile in the *next* scene's palette (a colour bridge). | Figr #14–17, Layo #47–48 |
| **Press → morph** | A sheen sweeps across the button (0.3 s), it scales to 95% and back, and the button becomes the resulting state card. | Layo #48–50 |
| **Tap navigation** | An in-app tap stands in for the cut: a grey dot presses, the screen dims, and the next screen is revealed. | Cosmos |

### B4. Line / path
| Name | Build | Seen in |
|---|---|---|
| **Follow the line** | A dotted trace, rail or connector extends and the camera trucks along it (300–500 px/s) to the next subject. | Adaline, Aside #85–92, Cloudflare #26–31 |
| **Crawler line with target pulse** | A 2 px line with a dot head and a grey trail (~15% of frame width) travels an orthogonal path (~1.2 s). On arrival it gives a ring pulse (0.3 s) and the target inverts to the accent colour. | Firecrawl #23–29 |
| **Construction pins** | Hairlines are drawn from an object's corners, a dot slides along each (0.3 s), and a pill pops up where the dot lands. Siblings are staggered 0.4–0.5 s. | Harvey #51–59 |

### B5. Layout / composition
| Name | Build | Seen in |
|---|---|---|
| **Re-centre on the key phrase** | After a sentence lands, slide it so the key phrase is centred while the other words fade out left to right (~0.07 s stagger). | Cosmos |
| **Word split, insertion** | Category words spread apart and images drop into the gaps, overlapping the words. | Cosmos #7–8 |
| **Hub reprise** | The same composition returns later with a new centre or new chips. Same layout, new meaning. | Harvey #28 → #95 |
| **Fixed-layout slideshow** | An identical layout with hard cuts every 0.5 s; only the content changes. | Cosmos #16–19 |
| **Before/after in identical framing** | The same prompt and the same device crop are shown twice: first failing, then succeeding. | Layo #13 / #54 |
| **Card slide-over** | A contrasting "with" card slides over the "without" card. | Cloudflare #77–78 |
| **Statement → header** | A centred claim moves to the top-left and becomes the section header, and the artefact that proves it builds below. | Raindrop #32–33 |

### B6. Camera / space
| Name | Build | Seen in |
|---|---|---|
| **Grid-cell dive** | Push about 2× into one cell of the ground grid (0.8 s ease-in-out). The cell reveals the next step. Repeat for a multi-step flow. | Firecrawl #101–109 |
| **Macro → context pull-back** | Open unreadably close (3×) on a label mid-typing, then snap out while the numbers tick. | Raindrop #21–23, Figr #58–59 |
| **Flat → 3D reinterpretation** | A flat square extrudes into a cube or box interior while the camera pushes 10–15%. | Harvey #46–47 |
| **Extrude into the machine** | A flat pixel formation tips into a 3D corridor. | Firecrawl #3–6 |
| **Rotational smear whip** | Rings spin ~90° per 0.5 s with directional blur, then cut to a still scene. | Flashback #50–51 |

### B7. Verb transitions (a transition that *is* the product's action)
| Product verb | Transition | Seen in |
|---|---|---|
| scrape / process | **Dither sweep:** a diagonal band (~30% of frame width) of accent halftone dots crosses in 0.6–0.8 s and leaves the processed version behind. | Firecrawl #56, #77, #110 |
| classify / evaluate | **Re-bin:** a character sphere's glyphs are re-sorted into benchmark bars. **Scanner sweep:** a bright vertical bar crosses in ~1 s. | Raindrop |
| decode / secure | **Glyph scramble** on key nouns only, 3–4 frames, then resolve. | Cloudflare, Aside ("encrypt$T") |
| search / step through | **Letter dropout:** 30–50% of letters vanish in one frame, then the new label fills in. | Merciv #56–63 |
| generate / write | **Hot text:** new tokens appear in an accent gradient and cool to grey over 0.5–1 s. | Veryfront #22–24 |
| connect | A **drawn cable** between two icons, glowing. | Lovable #24–27 |
| trace / observe | A **dotted trace line** carries the captions. | Adaline |
| chaos → order | **Stop-motion replacement** (6–12 fps) under a smooth camera, converging into a column or grid. | Harvey, Veryfront #12–14 |
| alert / monitor | **Dot → icon → rings larger than the frame → docks into a pill.** | Merciv #113–117 |

### B8. Melts and washes (weakest; use for chapter ends)
| Name | Build | Seen in |
|---|---|---|
| **Blur melt** | Blur the footage and overlays 0 → 60–80 px over ~0.5 s while grading toward the next ground. New type arrives 0.3 s later. | Conduit #57–58 |
| **Photo → blurred ground** | Push the last image to 3× and blur 0→80 px. The result stays as the background. | Conduit #4–5 |
| **Wash** | A 60–80% overlay in the ground colour covers footage, then dissolves off to reveal it. | Adaline |
| **Whiteout / overexpose** | Light bleeds from a screen, then everything goes to white. | Adaline #13–19, Aside |
| **Pixelate dissolve** | The ground breaks into ~2%-width mosaic blocks and fades. | Cloudflare #92–94 |
| **Staircase-pixel wipe** | A stepped accent wedge grows from an edge (~1.5 s) and covers the frame, cutting to the logo. | Firecrawl #120–124 |
| **Subtractive grid clear** | Tiles are removed 3–4 per frame in scattered order. The last one goes just before the logo appears in its spot. | Merciv #149–153 |
| **Sheet lift** | The top page flies out, motion-blurred and semi-transparent, and the stack moves up one slot. | Flashback #71–72 |

### B9. Hard cuts (allowed, with a carrier)
Use hard cuts only when the anchor, layout, light or rhythm carries continuity:
- on the beat of a type rhythm (Lovable);
- in a fixed-layout slideshow;
- a centred-anchor cut;
- a one-frame subliminal flash as a rhythmic accent (Firecrawl #64);
- tiny type → shout.

---

## C. Choosing: a decision guide
- **Viewer must read it?** Macro UI or type on ground, with a locked or slowly drifting camera.
- **Showing structure?** A deconstructed layout plus a follow-the-line camera.
- **Showing volume or scale?** A tilted plane, an accumulating field, a density ramp, or icons doubling per beat (1 → 2 → 4).
- **Showing a transformation?** A verb transition (B7), never a plain before/after cut.
- **Changing chapter?** A dot grows into the ground, or a melt. Change the ground colour.
- **The product's key button?** Push to the affordance, then either a zoom-through or press → morph.
- **Many parallel items?** A slot reel (text), a riffle (images), or a hub (UI chips).
- **Need energy without chaos?** Hard cuts with a centred anchor, or variant flips at 2/s on a slowly pushing card.

---

# Part 2: vocabularies added from the full 59-film study

## D. State vocabularies

### D1. Arrival states (how the newest element enters)
Pick one family per film, or one per *meaning*. Each is given with the films that use it.

| State | Build | Refs |
|---|---|---|
| Blur + low offset | 8–12 px blur and ~0.8 em low → 0 over 0.5 s (expo-out) | Figr, Cosmos |
| Ghost | Arrives at 25–40% opacity, resolves to 100% | Adaline, Layo, Perplexity, Google Pics |
| Karaoke / accent | Accent colour, fading to base colour over ~0.5 s | Aside |
| Hot text | The newest 5–6 tokens in an accent gradient, cooling to grey | Veryfront, Figma Shaders (in UI blue) |
| Highlight trail | A 30% brand-colour highlight behind the new phrase, fading over 1–1.5 s | Island |
| Glow-cool / colour temperature | A brand-colour bloom (15–25 px glow) cools to solid ink in 0.5–1 s, with no motion | iCloud+, LaunchAnything |
| Hue-cycle | Enters in a different transient hue each time for 1 frame, settles to the one accent | ChatGPT Work |
| Inverted block | The key word in a solid block, which drops out as the line re-centres | Raindrop, Flashback |
| Glyph scramble | The last 2–4 characters cycle random glyphs for 1–2 frames (mono) | Raindrop, Cloudflare, Lovable |
| Caret-typed | Per-letter with a caret; no blink while typing | Layo, Arena, Island, Index |
| Gradient wipe | An italic key word wipes in left→right through a soft gradient over 1–1.5 s, while the roman words are hard-on | Copilot |
| Light sweep | Glyphs start dark on black; a gradient light passes through them in ~0.5 s | Lovable, LaunchAnything |
| Oversize-settle | 150–250% → 100% (expo-out) | Lovable, AI Studio logo (2.5×), Material G (1.75×) |
| Undersize-rise | Enters at ~60% size, raised, then drops to the baseline | Herman Miller |
| Width-breathe | Variable width axis condensed (60%) → overflowing the frame (130%) → normal over ~2 s | Netflix |
| Annotation | A hand-drawn oval or underline in ~2 frames marks the key word | Instagram, Google Pics |
| Recolour on completion | Words append in white; the whole line turns brand colour when the last word lands | Figma Shaders |
| Mosaic resolve | An image arrives as 3%-wide blocks in tilted perspective and sharpens as the camera levels (1.5–2 s) | Sphinx |
| Random-letter fill | Letters appear in random order ("I NA URE") | Herman Miller |
| Kerning collision | Two words arrive touching and letter-space apart over 1 s | t0.ai |

### D2. Exit states (text and objects need exits too)
| State | Build | Refs |
|---|---|---|
| Backspace | Delete right→left at ~2× typing speed; the next line types into the same spot | Index, Arena, Zaro, ChatGPT |
| Editing verbs | Select-all (inverse block), italic toggle, delete (the caret turns red 1 frame before) | Arena |
| Blur-scatter | Per word: blur to ~10 px, lift 1–2%, rotate ±3°, 1-frame stagger L→R | Aurel |
| Staggered fade L→R with re-centre | Earlier words fade (~0.07 s stagger) while the survivor slides to centre | Cosmos |
| Occlusion by world | Passing foreground (clouds, branches) hides the type | Fable 5.1 |
| Shrink-out / grow-in | The old block shrinks to ~50% and drifts; the new one appears at that size and grows | Netflix |
| Tracking-out | Letter-spacing widens ~30%, then a cut | Apple |
| Dim to 20% | Outer words fade to 20% while the brand types in the gap | Aside |
| Dim-to-exit | A 1-frame luminance drop to ~50% after the final click, then a hard cut | Perplexity |
| Reverse-draw | Strokes and annotations erase along their path | t0.ai, Harvey |

### D3. Emphasis methods (choose by register)
- **Scale shout:** 25–60% of frame height, once in whisper films.
- **Whisper inversion:** the key claim at ~1/3 of body size, alone (Apple, Coca-Cola's "timeless.").
- **Polarity flip:** ink and ground swap for the key word (Netflix).
- **Semantic ground flip** on the clause (Apple).
- **Colour:** an accent, an inverted block, a highlight box.
- **Hand annotation:** a marker (t0), a proofreader (Apple), a pencil underline 0.5 s after the phrase (Index).
- **Voice change:** italic serif inside roman grotesk (Arena, Island, Copilot).
- **Behaviour:** a variable axis, a self-describing animation.
- **Camera:** a 15× macro on the word being typed (Spellbook).
- **Anxious dropout (inverse):** the key worried word sits on the brightest part of a blob and nearly vanishes (Superpower).
- **Luminance:** the only solid or bright element (Raindrop bars).

### D4. Anchor types (what stays fixed so cuts cohere)
| Anchor | Refs |
|---|---|
| A centred dot (3–4% of frame) | Harvey |
| A shape or silhouette: digit, eyepiece ring, mascot, pen tips on one point | Fable 5, Fable 5.1, keynote, Reve |
| A grid cluster, its count accelerating 1 → 40 | Blueprint |
| A spec-sheet HUD frame (corner ticks + chapter label) | OpenAI Brand |
| A soft-body stage atom (a bubble holding all copy, wobbling ±3–6%) | Opera Air |
| A semantic anchor (a mode pill, prompt box or hinge dot whose state causes each change) | Affinity, Index |
| A placement anchor (the mark at identical centre and size across real contexts; the same clock time on five devices) | Walmart, Shapes |
| Fixed type position with everything else flipping | Apple |

### D5. Annotation layers (a second voice)
| Layer | Build | Refs |
|---|---|---|
| Marker | Green brush strokes: a 1-frame nub, then the line, then the arrowhead. The arrow leads the camera, an underline emphasises, an X negates. Pink = wrong. The logo gets a 3-frame "boiling" burst. | t0.ai |
| Proofreader | A caret (^) at the insertion point; words hand-lettered on a 5–10° slant over 2–3 frames; parentheses; a checkbox ticked after the clause | Apple |
| Pencil | Scribble or underline under one word, 0.5 s after it lands | Index |
| Hairline reasoning | 1–2 px lines and small accent dots tracked to real motion (trajectory, climbing route, pose skeleton) | Claude Keep thinking |
| Arrow-label | A thin arrow + bold label; the label grows by a word, then a 2× push to the next subject | Wabi |
| Redlines | Blue padding and dimension specs on a component for ~1.5 s before it's used | Copilot |
| Construction | Hairline guides, registration marks and bezier handles appear before the content and fade after the lock-up | Flashback, Superpower, Arena |

### D6. Cursor and actor designs
- A named multiplayer pill per actor (Agent/Alex, Senior Partner). One colour per AI agent, introduced as pixel characters (Zaro).
- An oversized brand-coloured bevel (Veryfront).
- An avatar as the cursor (Lovable).
- A plain black dot, where a click = a 1–2 frame dwell (Copilot).
- A mobile tap dot (Cosmos).
- An emoji hand for TV UI (Netflix).
- Two cursors with different hand shapes drifting around a caption = collaboration (Google Pics).
- Collaborator names carried across shots (Lovable 2.0).
- The caret itself: colour by meaning (blue typing, red before a delete), shape by era (block = terminal, I-beam = editor).

### D7. Time and state devices
- A status-bar clock advancing (Cowork: 8:14 → 8:21).
- Closing a laptop lid as the time skip, with the screen glow persisting as the next ground (Cowork).
- Presence-coded grounds (Cowork).
- A running stopwatch across a cut (Burp).
- A real-time media ticker during a hold (Opera Air, Shapes).
- Odometer dates rolling (Wabi).
- Aspect-ratio mattes switched per cut for rhythm or archive feel (Keep thinking).

---

## E. Transitions added from the full study

### E1. UI-native
| Name | Build | Refs |
|---|---|---|
| **Component-as-wipe** | A real product component enters with its native motion and displaces the previous content (a pull-to-refresh spinner drops with overshoot 0.4 s, drags the title out 0.5 s, spins out 0.3 s) | Material, Uber |
| **Caption performs the feature** | The cursor clicks a word in the caption; the *word* undergoes the feature (boxed and lifted = isolate, recoloured, translated in place, marker-circled) before the UI appears | Google Pics |
| **Press → iris** | The headline collapses into an icon button; a hand presses it (squash, invert); the button circle opens as an iris onto the next screen | Netflix |
| **Icon portal** | Click an app icon; the app UI fades up behind it as the icon dissolves into place | Google Pics |
| **Icon-first pull-back** | Open on the feature icon at 40–50% of frame height, pull back ~5× in 1.5 s to find it's a toolbar button, and click on arrival | Lovable 2.0 |
| **Hover-driven preview swap** | The cursor hovering picker thumbnails is the cut; the background changes on the same frame | Figma Shaders |
| **Theme-swap reveal** | A 1-frame full tint wash, then the same layout in the dark theme | Material |
| **Mask swell** | A thumbnail's shaped mask scales 8% → 60% of the frame, goes solid, and bursts into the next chapter | Material |
| **Field → button → split-flap pill → icon** | A 4-station morph at one centre (fill wipe, split-flap roll, slot-rolled labels, contract to a squircle with a diagonal colour fill) | Google AI Studio |
| **Status-bloom colour bridge** | The "Generating…" glow matches the colour and position of the next shot's placeholder | Google Pics |
| **Status relay** | A fixed slot: the icon hard-swaps while grey verb text wipes in and out through a ~15% gradient mask, ~1.1 s per tool | ChatGPT Work |
| **Echo word behind status** | The status pill cycles verbs every 0.5 s while its noun sits huge (~50% of frame height) as a pale 8% outline drifting behind | Spellbook |
| **Checklist completion scroll** | A list scrolls one row per 0.5 s; dashed loading rings complete into checks as each row passes the upper third | Spellbook |
| **Object-as-word drag** | Drag a file icon labelled "data" into the sentence; it takes the noun's slot and typing continues | Island |
| **Self-editing title cards** | The product's UI (a chip, a marquee) edits the film's own kinetic type | Reve |
| **Diagonal-stagger → align** | In-progress steps enter offset +5% x; they snap flush-left when done | Cowork |
| **Status-log column → headline** | Process verbs append at 2 lines/s, older ones at 40%; the last stays put while the words around it become the next claim | Zaro |
| **Placeholder as thesis** | "Ask anything" → "Do anything" in one frame | ChatGPT Work |

### E2. Word and type-driven
| Name | Build | Refs |
|---|---|---|
| **Backspace slot reel** | The variable word is deleted and retyped instead of rolled; the prop set changes per word | Zaro |
| **Echo stack** | The key word duplicated into 4–6 stacked rows (offset or clipped, or one row struck through), held 1.5–3 s, resolving to one | t0.ai, Copilot |
| **Echo-letter onomatopoeia** | A vowel repeats 4–6× at −15% opacity each; the camera pans across, then it collapses to the word | Netflix |
| **Word truck** | A word at 40–60% of frame height, wider than the frame; the camera trucks across it in 1–1.5 s | Coca-Cola, Blueprint (6× + 10° tilt) |
| **Size-alternation anaphora** | A fixed lead word + a variable word flipping whisper (5%) ↔ shout (50%) every 0.5 s; the last one inverts | Coca-Cola |
| **Headline stack** | The previous line shrinks to ~40% and rises to 40% opacity while the new one ghosts in below | Netflix |
| **Match-cut ground inversion** | The same word, 1.2–1.5× larger, on the inverted ground, mid-sentence; the annotation continues | t0.ai |
| **Hinge-dot sentence** | Line halves are aligned either side of a centred atom; only the atom's contents change between clauses | Index |
| **Typing-history cascade** | 12–16 rows of the wordmark at every typing stage, mirrored, scroll ~3 s, then collapse to one row | Index |
| **Word-shuffle into logo** | The thesis words scatter and re-order, then collapse to the wordmark | Spellbook |
| **Self-describing adjective** | Each claim word is animated by the property it names | Uber |
| **Glyph-scatter → icon** | Title letters break into rotating strokes; 2–3 strokes re-form the feature icon (or icons morph into letters on a baseline) | AI Studio, Uber |
| **Letter sprout** | Selected letters shrink to dots and sprout icons that multiply into the next ground (~3 s) | Apple |
| **Acronym expansion** | "GUI" letters stay pinned while the full words type out around them | Wabi |
| **Specimen as copy** | The typeface is shown by typing adjectives about the brand, with live metadata rows | Arena |
| **Localised swap → in-world** | The same layout in 4 languages at 0.5 s each, then on a real billboard | Coca-Cola |
| **Aperture line reveal** | Each line appears through a window widening from its centre while the text slides inside | Netflix |

### E3. Grounds and fields
| Name | Build | Refs |
|---|---|---|
| **Glow-to-ground bloom (slow)** | A soft brand glow grows from behind a small card over ~2 s until it's the ground. Used as the climax. | Island |
| **Ink-blob flood** | An illustrated element (smoke) expands organically into the next ground | Apple |
| **Iris-close on the verb** | The ground becomes a disc shrinking 130% → 45% of frame height over 3 s while "…closing up" types inside | Index |
| **Dot iris → dot → logo** | The scene irises into one dot on a new ground; the dot splits into the mark | Zaro |
| **Palette-stripe wipe** | Brand colour bars sweep across; the last becomes the ground | Walmart |
| **Material wipe** | The world's substance (clay clouds) fills the frame ~1.5 s and parts | Mac mini |
| **Paper-tear ground change** | On a click, a torn-paper silhouette carrying the next texture appears behind the element | Medium |
| **Paper feed** | The ground advances like printer paper and delivers the logo | Index |
| **Error flood** | A bad cell spawns neighbours in a plus pattern, saturating the grid in 3 frames, then collapses to one good cell | t0.ai |
| **Gravity collapse** | A structured grid drops under rigid-body physics in ~1 s; the label lands tilted | Index |
| **Ground → logo shape** | The full-frame gradient blob reshapes into the logo silhouette over ~3 s | Lovable 2.0 |

### E4. Camera, space and portals
| Name | Build | Refs |
|---|---|---|
| **Instrument portal** | Push through a physical aperture; keep the ring as a vignette for 30+ s; exit onto the *real* version of the last thing seen, at the same frame position | Fable 5.1 |
| **Push through the device screen** | The switch from the hardware world to the app world | Perplexity |
| **Lid-close time skip** | Pull back to the laptop, warm the screen to sunset, close the lid (~1 s); the glow becomes the next ground | Cowork |
| **Rewind reset** | The film's own opening plays backwards at 2–3× with horizontal smear for 1–1.5 s ("start over") | Burp |
| **Specimen flies at the lens** | Composition parts take off in a stagger toward the camera; one fills the frame and uncovers the title | Fable 5 |
| **Pull-back asset wall** | A finale grid of every image used; pull back, then cut to the lone logo | Coca-Cola |
| **Output-wall collapse** | Dozens of outputs on 4–5 depth layers; pull back ~5×, then collapse to one card outline | Arena |
| **Carousel → pile → URL** | Outputs on a curved 3D plane converge into a pile that shrinks as the URL blurs in | Google Pics |
| **Scene → grid tile → other tile expands** | A two-way nest through a collage | Walmart |
| **Crop-to-word shout** | Open on a letter crop at 80% of frame height, then a ~5× pull-back in one frame | Walmart |
| **Split reveal: plan vs real** | A hard vertical or diagonal split with the drawing on one side and the photo on the other, the title block across both; rotate the axis each time | Blueprint |
| **Slit-open testimonial** | Video opens from a narrow vertical slit into a card with handles and a waveform | Sphinx |
| **Continuous set, cutting screen** | Hold one device set with moving ambient light; cut only the screen content every 0.5–1 s; tighten 1.3× every 2.5 s | LaunchAnything |

### E5. Riffles and montage
| Name | Build | Refs |
|---|---|---|
| **Same-subject treatment riffle** | A fixed subject position and scale; swap material or style every 0.5 s for 4–10 variants; end on the canonical version | Affinity, Figma, OpenAI Images, Herman Miller |
| **Found-glyph riffle** | The key glyph built from real objects in 20–40 media; identical centre and scale; hard cuts at 2/s; zero camera motion | Fable 5 |
| **Diegetic word riffle** | Each word of the sentence set inside a different photographed or generated surface, 0.5 s each | OpenAI Images |
| **Shape-rhyme chain** | Cuts ordered by line structure or radial form, not subject | Fable 5.1 |
| **Diegetic word inventory** | One noun present physically in 13+ materials and typefaces, near centre, 0.5–1 s each | Keep thinking |
| **Hidden-subject hold ladder** | Unreadable macro crops with holds shrinking ×0.8 (4.5 s → 0.5 s) | Fable 5 |
| **Costume riffle / escalation** | A fixed central character or product; costumes cut at 2/s, or each benefit grows from the body | keynote, Mac mini |
| **Word-per-cut essay** | A caption changes on every cut at ~2 words/s; variety comes from switching type systems | Wabi |
| **Black breath** | End the fast act mid-action; 2.5 s of black with grain; open on the aftermath | Keep thinking |
| **Recall collage → subtraction** | Gather every earlier prop around the border, then remove them all at once, leaving one word | Shapes |
| **Attrition grid** | People tiles grey out for a frame, then vanish 1–2 at a time | Shapes |
| **Shrinking-history funnel** | Successive artefacts, each 25–40% smaller, converge to where the product's primitive is born | Affinity |
| **Pain montage** | Multiplying error dialogs (2 → 8 → 12 in 1.5 s) as a rhetorical before | Affinity |
| **Two-render frame flicker** | The object alternates between two renderings every frame as it jumps = instability | Sphinx |

### E6. People, logo and product
| Name | Build | Refs |
|---|---|---|
| **Captions behind the speaker** | Words at 12–15% of frame height composited behind the rotoscoped head, alternating sides | Sphinx |
| **Stipple → footage** | A person is introduced as a dot cloud (the brand atom), crossfading to footage over ~1 s | Sphinx |
| **People → UI shrink** | A row of face circles shrinks ~4× into the app's avatar stack | Lovable 2.0 |
| **Caret-born mascot** | The caret blinks, squashes to an underscore, inflates into the character; it returns to type the lock-up | Claude keynote |
| **Logo shatter / reassemble** | The mark splits into primitives that become every scene's particles; the reverse paths rebuild it | iCloud+ |
| **Converge to mark** | Scattered logo primitives on a grid slide into formation | Copilot |
| **Outline → fill wordmark hinge** | A 1–2 px outline with bezier anchors, trucked across the last image, fills with the gradient (0.3 s) and whites out | Superpower |
| **Atom → label → chain** | The swoosh draws on, wraps the product as its label, then duplicates into a chain | Coca-Cola |
| **Logo-shaped aperture** | Footage seen only through a window shaped like the mark between two words; its facets change with each clip | Spellbook |
| **Survivor tray** | A dock of generic icons contracts until only your icon remains | Aurel |
| **Inline thumbnail ↔ stage bookend** | The image in "Brand [img] Product" stretches into the stage; at the end a different image collapses back into the slot | OpenAI Images |
| **Ingredient insertion + jolt** | The spec as a physical chip lowered into the product, with a 1-frame hand-drawn lightning bolt | Mac mini |
| **Rim-lit silhouette** | A dark body with a highlight travelling around its bevel for ~3 s instead of a push | Perplexity |
| **Still → alive** | The generated still simply starts moving under a 10% push | Burp |
