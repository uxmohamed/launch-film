# Conduit — analysis (186 frames, ≈93 s)

## 1. One-line concept
Conduit is an "AI workforce built for hospitality". The film is a founder-led pitch built as **problem → culture/hype → "chatbots aren't enough" → agents that do the work → product demo (Reply/Research/Memorize, Quote/Negotiate/Book, unified inbox, Operator) → social proof numbers → CTA**. It runs like a documentary. Two founders talk to camera, and kinetic captions plus floating UI are laid directly over the talking-head footage.

## 2. Visual world
- **Three alternating surfaces:**
  1. Pure white type cards (#1–4, #13–19, #129–134).
  2. Heavily blurred photographic gradients: green/teal (#5–9, #179–186), pink→orange (#10–12), orange/teal with visible fine contour/moiré lines (#58–65).
  3. Shallow-DOF founder interviews in bright offices with bokeh backgrounds.
- **The gradients are real hotel photos blurred to mush.** You can see this at #5: the resort photo from #4 scales up to full frame and blurs, and that blur becomes the backdrop. The gradients carry a faint topographic line texture (visible #58–62, #180–185), which reads as "printed" rather than CSS.
- **Type:** light-weight neo-grotesk (Inter/Söhne-like, weight ~300–400), sentence case. Hero captions sit at ~4–5% of frame height (#9 "Travellers expect instant responses" ≈ 55 px cap height on 1080). The wordmark "conduit" is a rounded geometric bold in white. An emphasis word gets an orange accent colour ("every", #129–131).
- **UI staging:**
  - (a) Tiny white chat bubbles scattered at various depths over a gradient, with depth-of-field blur on the near ones (#6–8).
  - (b) **Split layout:** a white left column with a feature list (Reply/Research/Memorize) beside a portrait-cropped panel of blurred sky/grass photography, with UI cards floating on it (#76–114).
  - (c) A full-bleed desktop inbox on a pale blue-to-sand gradient, cropped and zoomed (#115–128).
  - (d) An Operator chat panel docked to the right third over interview footage (#144–160), like a picture-in-picture HUD.
- **Motifs:** an orange "Agent" cursor-pill and a blue "Alex" cursor-pill (Figma-style multiplayer cursors) stand in for the AI agent and the human. Pastel sticky-tag chips name tasks. Frosted glass circles hold departments. Logo chips are white pills.

## 3. Shot list
| Frames | ~s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–4 | 2.0 | Type card, white | Small hotel photo centred; "Hospitality" enters left, "is changing" right | static | Photo **swaps content every frame** (lobby→atoll→cabin→palace) while growing ~0.35→0.55 of frame height; stacked "deck" edges show behind it; "is" then "changing" fade in with a luminance ramp (#3 "ischanging" half-grey) | The photo scales up to full frame |
| #5 | 0.5 | Zoom-through | The resort photo fills the frame and blurs heavily | push-in ~2.5× | Blur ~60 px ramps in | The blurred image *becomes* the gradient BG |
| #6–9 | 2.0 | Gradient + floating bubbles | "Travellers expect instant responses"; ~8 guest-message cards | slow push; cards drift outward | Cards travel radially outward and grow (near ones blur and leave the frame at #8–9); headline scales ~0.9→1.1 | Colour-shift dissolve to pink/orange |
| #10–12 | 1.5 | Gradient card | "across all [channel icons] channels" | static | Icons pop in as a clustered row with red notification badges; the text slides apart to make room | Cut to white |
| #13–19 | 3.5 | White + interview cutout | Founder in small rectangle; per-word captions "I / do not / think / a chatbot / is the right interface / for travel" | static | Caption replaced word-group by word-group, centred below the video. Chat-input field ghosts (grey "Hey, how can I help you?" boxes) fade in around the frame at #15 as a "chatbot everywhere" field | #19: video removed, only the caption stays |
| #20–31 | 6.0 | Found-footage montage | News anchors, CNBC "TECH CHECK", "AGENTIC AI INFLECTION POINT", keynote "World models", a tech CEO in a leather jacket | clip-native | Small captions ("there are thousands… on the market") placed left and right in empty space | Hard cuts every 1–2 s; #32 fade to near-black |
| #32–57 | 13 | Founder A interview (Cole Rubin) | Lower-third name blur-in; chat bubbles; checklist; arcs; task tags | locked, slight drift | See details: lower-third, bubbles, checklist, a big white arc drawing in a semicircle (#44–48), then pastel tags populating (#50–57) | Tags + footage **dissolve into blurred orange/teal gradient** (#58) |
| #58–65 | 4.0 | Logo reveal | "conduit" + "AI workforce built for hospitality" | slow push (logo ~1.05→1.0) | Tagline fades in #61; hotel photos slide in from the edges as a collage frame (#63–65) | Cut to interview |
| #66–71 | 3.0 | Founder A | Frosted circles "Concierge / Sales / Finance / Marketing" connected by thin dotted lines | subtle push-in | Circles fade and scale up from ~0.7, staggered ~1 frame apart, then orbit/drift slightly | Cut |
| #72–75 | 2.0 | Founder B (Punn Kam) | Name lower-third blur-in; a chat bubble "Is it possible to get a late checkout?" with an "M" avatar | static | Bubble enters from the right; at #75 **a white left column wipes in over the footage** | Wipe to split layout |
| #76–101 | 13 | Split feature demo | Left: Reply · Research · Memorize (the active item gets a bullet and turns black). Right: portrait panel with UI | inner panel content scrolls up | Dark agent reply bubble types in (#77–78). The panel blurs its contents out, then the orange Agent cursor enters (#79) and clicks booking rows. A chat thread scrolls upward (#84–91) with a star-rating card. #92 empty. Then a guest profile card with chips; the cursor adds preference chips (#93–95); an "Upcoming stay" card stacks below (#98–101) | Cut to interview |
| #102–104 | 1.5 | Founder B | — | static | — | Cut back to split |
| #105–114 | 5.0 | Split demo 2 | Quote · Negotiate · Book; a quote conversation, then a room-grid calendar | panel content scrolls | The previous list words slide/fade out as the new ones fade in (#105 shows "Quote/Negotiate" ghosted). The calendar grid fades in from blurred (#112) to sharp (#113) | Crossfade to inbox |
| #115–128 | 7.0 | Inbox, full-bleed | Todo list; Alex cursor moves to row 2; a zoomed conversation; the escalation options; caption "The conversation escalates in our [unified inbox]" | **zoom-in 1.0→~1.6 then pans** to the options (#124–127) | The caption word "unified inbox" sits in a white chip. The Alex cursor clicks "Partial refund…" (the row highlights blue at #124) | Caption fades (#124), then the whole frame washes to white (#128) |
| #129–134 | 3.0 | White type card with faint concentric line pattern | "Behind every guest facing agent is…" → ✳ → "✳ Operator" | static | "every" in orange; the second line fades in; the text clears to leave only the asterisk; "Operator" slides out from behind the asterisk to the right | The asterisk stays centred as an anchor |
| #135–138 | 2.0 | Integration orbit | App icons (Salesforce, Teams, Snowflake, Drive, Outlook, Slack, Gmail, WhatsApp) orbit the asterisk tile | static | Icons fade in scattered and blurred, then rotate ~30° around the centre (#136→137). At #138 they collapse into the centre with blur | Collapse → cut to interview |
| #139–160 | 11 | Founder B + Operator HUD | Operator panel slides in from the right (#144–145); the prompt types; the reply streams in and scrolls; "Knowledge base updated / Agent updated" confirmations | cut from wide to medium close (#143→144) | Typewriter prompt (#146–148). The bubble moves up into the thread (#149). The long answer streams in and auto-scrolls (#151–157) | Panel slides off right (#160) |
| #161–178 | 9 | Founder B wide + stats | "300+ Hospitality Brands & Hotel Groups" → "100k+ Live properties" → "50M Guest conversations"; logo pills | static | Big number centred over his torso with a subtitle beneath. Logo pills pop in around it in clusters of 2–4 per frame (#166–170). Numbers swap by blur dissolve (#170 "300+" ghosting under blur) | The whole frame **blurs into the green gradient** (#179) |
| #179–186 | 4.0 | End card | "Start today at conduit.ai" → "conduit" | static | The URL fades out (#183), the wordmark fades in (#184); final frame washes to pale | Fade to white |

## 4. Transition inventory
- **Photo carousel → zoom-through → blur = gradient** (#4→5). The hotel photo becomes the atmosphere. Motivation: "hospitality" literally becomes the environment.
- **Radial fly-out of UI bubbles** (#6→9): cards fly past the camera, clearing space for the headline. Near-plane cards pick up blur, simulating DOF.
- **Hue-shift dissolve** between gradients (green → pink/orange, #9→10).
- **Caption-only bridge** (#18→19): the video vanishes and the caption "for travel" holds alone, then a hard cut to found footage.
- **Hard-cut montage** of news footage (#20–31) → **fade through black** (#32) into the founder.
- **Footage → blurred gradient** (#57→58 and #178→179): the live-action frame is blurred and colour-graded into the brand gradient. Used twice, as a "chapter end" device.
- **Panel wipe** (#75→76): a white column slides in from the left over the interview. The chat bubble already on the footage carries over into the demo panel (object carries over).
- **List-item swap** (#104→105): the old feature words fade to grey and slide off as new ones arrive, keeping the same layout slot.
- **Blur-in of a UI component** (#112→113): the calendar resolves from blur.
- **Wash to white** (#128→129) → the type card's asterisk becomes the **anchor** for the next scene (#132–138).
- **Orbit collapse** (#137→138): icons implode into the asterisk tile, then cut.
- **Wide→MCU cut** on the same founder (#143→144) to make room for the HUD.

## 5. Easy-to-miss details
- #1–4: the **photo changes every 0.5 s while its frame keeps growing**, and a darker "stack" of cards peeks behind it. It reads as a riffle through a deck of hotel photos.
- #3: "ischanging": the second word arrives with no space yet and at 50% grey. Words fade in with a left-to-right luminance sweep, not an opacity pop.
- #6–8: bubbles are at **three depth planes**. Far ones are tiny (~5% width) and sharp, near ones ~15% width and blurred ~8–12 px. Parallax rate differs by plane.
- #33–36: the lower third "Cole Rubin / Founder" drifts left and blurs out over ~4 frames. Exit = slide ~40 px + blur, not a cut.
- #37–39: grey message bubbles float in the upper left at low opacity (~40%). The key reply "Thanks for your message. We'll get back to you soon." sits at 100%. The contrast emphasises "the ones that respond" (bots that only reply).
- #40–42: the checklist items ("Booked a 12-room block", "Comped a VIP upgrade", "Responded to 45 reviews", "Refunded per policy", "Generated nightly report") check in **one per frame from the top**, then fade from the bottom up (#42 has only the last ghost left).
- #44–48: a thin white arc (~3 px) draws clockwise around the founder's head as a semicircle, with a tangent line flicking off at #46. It then fades while still expanding (#48). A pure gestural beat that punctuates the sentence, with no data behind it.
- #50–57: task tags ("Refund", "Rebooking", "Dispatch", "Maintenance call", "Upgrade", "Charge", "Room block", "Loyalty") appear 1–2 per frame, **in different sizes (3 scales) to imply depth**, each in a different pastel.
- #58: some tags are still visible through the blur during the dissolve into the logo. Content never cuts cleanly; it melts.
- #63–65: the hotel collage enters from the frame edges and keeps drifting outward ~2% per frame (an expanding frame around the logo).
- #66–70: department bubbles are **frosted glass** (backdrop blur + 1 px white stroke) with thin dotted connectors, placed in the negative space right of the speaker. The founder is framed off-centre left specifically to leave that space.
- #79: the Agent cursor is an orange arrow with an "Agent" label pill. Before it enters, the underlying rows blur out briefly (#79 frosted), then resolve with the cursor on them. Blur is used as a "loading" state.
- #80–82: the cursor moves from row 1 → row 2 over 2 frames, and the row it's on gets a subtle lift.
- #93–95: the list bullet advances to "Memorize" **exactly when** the cursor starts adding preference chips. The left nav is synchronised to the right-panel action.
- #116–118: the blue "Alex" (human) cursor hovers over the row "Esther Rubin" and drifts ~40 px over 3 frames. It's alive, not parked.
- #119–127: the zoom goes into a stylised conversation, then pans right-down to the options. The caption's key noun is in a chip ("unified inbox") in the same white as the UI, tying text to UI.
- #146–148: the prompt types into the input at ~40 chars/frame (fast). The reply streams in and auto-scrolls. Scroll speed is ~one paragraph per frame.
- #166–178: logo pills vary in size and a few are cropped by the frame edge (#169 "ROBSON" at the right edge). Stat numbers are ~8% frame height, white, over the speaker's chest, with no backing plate. The footage is dimmed ~20% to hold legibility.
- The end card holds the URL ~2 s and the wordmark ~1 s. The last frame lifts to pale (fade to white, not black).

## 6. Pacing curve
Fast open (#1–12: ~6 s, 4 ideas, photos swapping every 0.5 s) → thesis slows to spoken words (#13–19) → **fastest section** in the news montage (#20–31, cuts ~1 s) → breath in the founder (#32–57, long take with graphics pulsing every ~2 s) → brand beat (#58–65) → demo mid-tempo (13 s + 5 s + 7 s blocks, each with one cursor action every ~1 s) → reset on white (#129) → integrations burst (2 s) → longest calm stretch in the Operator HUD (11 s) → stats crescendo (3 numbers in 9 s, logos accumulating) → quiet end card, 4 s. The climax is the accumulating logo field under "50M".

## 7. What makes it premium
- The talking head is **the canvas**, not a separate segment. UI, tags, arcs and stats occupy the negative space the DOP left in the framing.
- Every gradient is derived from real hotel photography, so brand colour and subject stay coupled.
- Two named cursors (Agent orange, Alex blue) personify AI vs. human without a line of explanation.
- A three-verb nav (Reply/Research/Memorize → Quote/Negotiate/Book) structures the demo like chapters. The UI is re-built simplified, not screen-recorded.
- Found news footage borrows cultural urgency cheaply and legitimately, placed before the product.
- Chapter ends use a blur-melt, never a wipe. The film feels continuous.

## 8. Reusable techniques
1. **Photo riffle → blur-bloom BG.** Centred photo at 30% height; swap the image each 12 frames (at 24 fps) while scaling 1.0→1.6 (ease-in). On the last image, push to 3× and Gaussian-blur 0→80 px over 10 frames. Keep the result as the scene background. Add 2–3% noise or contour texture.
2. **Radial UI fly-out.** 6–10 small cards around the headline on 3 z-planes. Animate z outward over 1.5 s (linear-ish). Near-plane cards get 10 px blur and exit the frame; the headline scales 0.92→1.05.
3. **Negative-space HUD over interview.** Frame the speaker at the left third. Add frosted circles or tags in the right two-thirds. Stagger entrances 2–3 frames apart, scale 0.7→1 with a slight overshoot, and dissolve out on a blur.
4. **Named multiplayer cursors as characters.** Arrow + label pill, distinct colours for agent and human. Keep the cursor moving 20–40 px during "holds". Every click triggers a row highlight.
5. **Synchronised verb-nav split layout.** A left column of three stacked verbs (active = black with bullet, others 40% grey) and a right portrait panel. Advance the verb on the same frame the panel action changes. Swap verb sets with a grey-out and slide.
6. **Blur-melt chapter break.** Blur the footage and overlays 0→60 px over ~0.5 s while grading toward the brand gradient. Type (logo or URL) fades in on top 0.3 s later.
7. **Stat over person with accumulating logo field.** Big number centred at ~8% height with a small subtitle. Logos pop in 2–4 per 0.5 s around it and stay. Numbers change by blur-dissolve while the logos persist, so the field only grows.
8. **Asterisk anchor.** Clear a type card down to a single glyph, then slide a product name out from behind it. Reuse the glyph as the hub of an integration orbit that rotates ~30° and implodes.
