# Crosscut B — Conduit (≈93 s), Merciv (≈80 s), Veryfront (≈30 s)

## Recurring patterns

1. **One continuous task threads the whole demo.**
   - Conduit: a guest's late-checkout request → reply → research → memorize → quote/book → escalate → operator.
   - Merciv: one skincare query → sources → cited answer → tracker → alert → files → Slack.
   - Veryfront: build an agent → use it on one contract → "approved".
   - None show a feature grid. Each feature is a *step* in a story about one object (a message, a query, a contract).

2. **Brand atom reused as the transition engine.**
   - Merciv: dot → logomark bar → "o" of "on" → alert icon + rings.
   - Veryfront: gradient sphere → azure dot → chapter-card flood → agent icon → back to sphere.
   - Conduit: asterisk ✳ → Operator logotype → integration hub.
   - In all three, a single glyph is carried across 3–5 scene changes.

3. **Cursors as characters.**
   - Conduit uses labelled multiplayer cursors (orange "Agent", blue "Alex").
   - Veryfront uses a giant brand-blue bevelled cursor.
   - Merciv uses the macOS pointing hand at native-ish scale.
   - In all three, the cursor is never parked. It drifts 20–40 px during holds, and its clicks trigger the next state.

4. **Word-append kinetic type.** All three build sentences one word or word-group per 0.5 s frame, re-centring each time: Conduit "Hospitality / is changing", "I / do not / …"; Merciv "Every / great brand"; Veryfront "Your agent / is ready". None use per-letter animation for headlines. Per-letter appears only for wordmarks (Merciv) and UI typing.

5. **Rebuilt, simplified UI, never raw screen recording.** Components are isolated on a flat field (paper, grey, blurred photo) and cropped to macro. Unrelated chrome is removed. UI type is enlarged to 3–5% frame height for legibility.

6. **Blur as a state and transition medium.**
   - Conduit melts footage into gradients at chapter ends and blurs panels as a "loading" state.
   - Merciv blurs the source-step labels and Slack reveal lightly.
   - Veryfront uses DOF blur for selection and blur-in for the result card.
   - Blur magnitude ranges from 6–12 px (selection/DOF) to 60–80 px (scene melt).

7. **Photo riffle under or around type** (Conduit #1–4, Merciv #7–10): the image changes every frame (0.5 s) while the type or frame holds. It establishes the category's taste in about 2 s.

8. **Collage fill ↔ subtractive clear.** Merciv fills from the edges and clears to a hero, and at the end clears a grid tile-by-tile. Conduit frames the logo with an edge collage (#63–65) and grows a logo field around stats. Things accumulate at the edges and the centre stays reserved for the message.

## Contradictions (opposite choices, and why)

- **Human vs. no human.** Conduit is founder-led, with interview footage as the canvas and UI as a HUD in negative space, because trust matters in hospitality and the founders are the brand. Merciv and Veryfront have zero humans except UI avatars. Their buyers (brand strategists, ops teams) want to see the tool, and the films run silent-friendly.
- **Camera.** Merciv moves the camera constantly (caret-follow, pull-backs, pans across documents). Veryfront keeps a locked camera with in-place card swaps, plus a single 8× zoom punch. Conduit sits between them: a locked interview camera with slow zooms and pans inside UI panels. Merciv's content is long text, so the camera must travel. Veryfront's wizard is a fixed modal, so stillness reads as "simple".
- **Colour temperature and background.** Merciv uses warm paper plus editorial photography (fashion/beauty vertical). Conduit uses photo-derived blurred gradients (hospitality, place). Veryfront uses flat synthetic azure and grey (enterprise tool, abstract). Each background is derived from the customer's world.
- **Type scale drama.** Merciv swings from 1.5% to 25% frame height for emphasis. Veryfront keeps every title ~7% and never shouts. Conduit keeps captions ~4–5% and gets emphasis through colour ("every" in orange) or a white chip ("unified inbox").
- **Endings.** Conduit fades to white after the URL → wordmark order. Merciv shows the logomark, then the wordmark, then the URL, with a 3 s hold. Veryfront replays its intro exactly (palindrome, loopable, no URL).
- **Social proof.** Only Conduit uses stats (300+, 100k+, 50M) and logos. Merciv substitutes "1782 considered / 1028 sources" as in-product proof. Veryfront has none.

## Numbers and ranges (at ≈0.5 s per frame)

| Metric | Observed range | Examples |
|---|---|---|
| Opening title/logo | 1.5–2.5 s | Veryfront #1–5 (2.5 s); Merciv 1.5 s of blank + 1.5 s first words |
| Chapter / interstitial type card | 1.0–3.5 s | Veryfront 1–1.5 s; Merciv "Data changes fast…" 3.5 s; Conduit "Behind every…" 3 s |
| Word-append cadence | 1 word-group per 0.5 s | all three |
| Photo riffle | 1 image per 0.5 s, 4 images | Conduit #1–4, Merciv #7–10 |
| Single UI action beat (hover → click → state) | 1.0–2.0 s | Veryfront wizard steps; Conduit cursor clicks; Merciv Track button |
| Typing speed (UI) | 6–8 chars per 0.5 s (legible macro) to 40–60 chars per 0.5 s (prompt dumps) | Merciv query (slow, it's the plot); Veryfront/Conduit system prompts (fast, it's texture) |
| Counter tick | 6–7 values over 3–5 s, ease-out | Merciv 9→1028 sources |
| Stat hold (number on screen) | 2–3 s each | Conduit 300+/100k+/50M |
| Macro zoom factor | 2–4× typical, 8× for a single punch | Merciv typing ~3×; Veryfront send button ~8× |
| DOF blur on non-selected | ~6–12 px @1080p | Veryfront tiles, Conduit bubbles |
| Scene-melt blur | ~60–80 px over 0.5–1 s | Conduit #57→58, #178→179 |
| Staggered children | 1–4 items per 0.5 s | Conduit tags/logos, Merciv tracker rows, Conduit checklist 1 per frame |
| End card hold | 2.5–4 s | Veryfront 2.5 s, Conduit 4 s, Merciv 4 s |
| Longest single continuous demo act | 7–13 s | Conduit split demo 13 s, Merciv typing+sources 10.5 s, Veryfront usage 7 s |
| Share of runtime that's product UI | ~45% (Conduit), ~75% (Merciv), ~80% (Veryfront) | — |

## Takeaways for the manual
- Pick one object and follow it. Carry a single brand glyph through every chapter break.
- Typing speed should encode importance: slow if the viewer must read it, a blur of text if it's just "the AI is writing".
- Macro-crop UI at 2–4×, saving one extreme zoom (6–8×) for the climactic click.
- Use blur at two magnitudes: small (8 px) for focus and selection, huge (60 px+) for chapter melts.
