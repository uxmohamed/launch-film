# Google AI Studio (custom URLs), analysis (84 frames, ≈42 s)

## 1. One-line concept
A single-feature teaser for custom URLs on apps published from Google AI Studio. The spine is one app, "Atelier Menu Studio", followed through one flow: Publish button → publish dialog → type the URL slug → "Available" → "Publish your app" → loading pills → app icon → "is published" → live in a browser tab at `atelier.ai.studio` → "Grab your custom URLs today" → URL end card. The followed object is the **URL string**. The product's own multicolour Gemini gradient is the atom, used as a **glowing border** that travels from field to button to icon to horizon.

## 2. Visual world
- **Ground:** pure black throughout (#1–#84). No texture and no grid. The "world" is light: a blurred Google four-colour gradient (blue, green, yellow, red) appears as (a) glows leaking at the frame edges behind the dialog (#22–#25), (b) a 1–2 px **animated gradient stroke** around the focused control (#31–#52), whose hue rotates frame to frame (#33 pink/orange → #34 blue → #35 teal → #36 yellow-green → #37 red → #38 blue), and (c) a soft 40–80 px outer glow halo under the control that picks up the stroke colour (#40, #43, #45).
- **Type:** Google Sans, regular weight, white or 60% grey. Title type ("Introducing", "custom URLs") has a cap height of ~7–8% of the frame, much bigger than the manual's 1.5–3.5%. The URL field at macro scale (#35–#36) has a cap height of ~10%. The end card URL is small (~3%) and 70% grey.
- **Imagery:** real dark-theme UI of AI Studio (toolbar, publish modal, form), always dark on black, so window edges nearly vanish. One iconic 3D-ish moment is the **rainbow aurora horizon**: a curved dark planet-like arc under a spectral sky (#57–#61). This is "published to the world" drawn as a sunrise.
- **Staging:** starts at a real toolbar crop with a tilt (#16–#18, the window is slightly perspective-rotated and enters from bottom-left), then a real modal, then **UI dissolved into single controls floating on black** (#31–#56). Chrome is removed progressively until only one pill is left. Browser chrome returns only for the payoff (#62–#71).
- **Cursor:** the stock macOS arrow, recoloured Google blue with a white outline, scaled large (~5% of frame height at macro, #43–#45).

## 3. Shot list
| Frames | ≈s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–#3 | 1.5 | Title | "Introducing" | locked | **blur-in with a spectral colour fringe**: #1 heavily blurred (~30 px), letters tinted by the rainbow; #2 sharp left, "ng" still blurred yellow (left-to-right focus sweep); #3 fully sharp white | letters scatter |
| #4–#6 | 1.5 | Letter break-up | the letters of "Introducing" fly apart and rotate (#4 two "n"s tumbling; #5 a "c", an "ı" stroke and a hook) | locked | glyph fragments rotate 30–90° and drift outwards; the hook and "c" shapes **re-assemble into the link glyph** at centre (#6) | icon becomes a word |
| #6–#10 | 2.5 | Feature name | "custom 🔗 URLs": the link icon sits inline as a word | locked | #6 icon sharp, "m" blurred on the left; #7 "custom" blur-in with a warm fringe, "U" blurred; #8 sharp; #10 whole line **scales down ~50%** while a blue glow rises bottom-right | scale-down + blur |
| #11–#15 | 2.5 | Brand | AI Studio logomark large and blurred (#11, ~25% of frame width), then shrinks and sharpens; "in" appears left (#12); "Google AI Studio" blur-in left→right (#13–#14); "in" slides away and the lockup re-centres (#15) | locked | oversize-settle on the logomark (≈2.5× → 1×) | cut to UI |
| #16–#18 | 1.5 | Toolbar | tilted dark window rising from bottom-left: Remix / Share / **Publish** | window drifts up-right ~5%, the tilt flattens | cursor arrives on Publish (#17), clicks (#18, the button lightens) | push |
| #19–#20 | 1 | Nav | the toolbar pushes in (Chat / Share / •Publish / Versions / Secrets); a modal appears | push ~1.3× and pan right | modal rises | settle |
| #20–#26 | 3.5 | Publish modal | "What does publishing look like?", a mini "Your app" card with a **rainbow gradient border**, two bullets, a white "Get started" button | slow upward pan (~15% over 6 frames) plus push | edge glows bloom in at the frame sides (#23–#25); cursor to Get started (#23), click (#24–#25); the button detaches and slides up as the form scrolls in beneath it (#26) | scroll |
| #26–#30 | 2.5 | Form | App name "Atelier Menu Studio", description paragraph, App URL "atelier-menu-studio" + ".ai.studio", "Publish your app" button | slow push ~5% | cursor drifts from the description to the URL field (#29–#30) | UI dissolves |
| #31–#32 | 1 | Isolate | everything but the App URL field fades out; the field gains a gradient stroke | locked | the rest of the form fades out over ~2 frames | zoom-in |
| #33–#37 | 2.5 | Macro typing | field at ~4× (cropped by the right edge): empty (#33) → "ate|" → "atelie|" → "atelier|" | camera pushes then **pulls back** (#36→#37 scale ~1.3→1.0) | gradient stroke hue-cycles each frame; caret blinks; "Available" appears in green below after typing stops (#37) | reflow |
| #38–#42 | 2.5 | Suffix reveal | ".ai.studio" slides in to the right of the field in 40% grey; the field + suffix group re-centres | slow drift right-to-left | colour glow under the field grows and moves around (orange → violet → green) | button swap |
| #43–#46 | 2 | Button | the field **morphs into the button** in place: white fill wipes in left-to-right (#43, a white bar ~80% across); "Publish your app" (#44); cursor clicks (#45); the camera drifts left and the cursor exits up (#46) | drift ~10% | fill wipe ~0.5 s; glow under the button pulses | press |
| #47–#52 | 3 | Loading pills | the white button **flips/rolls** into a dark pill (#47, the white face slides up and away like a split-flap); "Setting up domain" (#48–#50) → "Publishing your app" (#51–#52) | slow drift | pill label changes by a slot roll; the glow stroke keeps rotating | pill contracts |
| #53–#56 | 2 | Icon birth | the pill contracts to an empty dark squircle (#53); a line-art rocket draws (#54–#55); a coral fill **wipes diagonally** across the tile (#56) | locked | rocket tilts ~15° between frames (a small launch wobble) | icon lands |
| #57–#61 | 2.5 | Published | the app icon (coral with fork/knife glyph) on a black curved horizon; the rainbow aurora **rises behind the horizon** (#57 none → #59 full); "Atelier Menu Studio is published" blur-types left→right (#57–#59) | slow push ~10% (#60→#61 icon grows ~1.3×) | aurora grows upward; text blur-in per word | shrink into UI |
| #62–#66 | 2.5 | Context | the published card shrinks back into the real AI Studio right panel inside a full browser window (#62 cropped, then #63–#65 the whole window on black at ~70% of frame width) | pull back ~3×, then locked | cursor clicks the "Visit app" button (#65–#66); the panel's aurora smears/blooms bottom-right on click (#66) | cut |
| #67–#70 | 2 | Live app | a browser tab "Atelier Menu Studio", URL bar `https://atelier.ai.studio`, the real menu-builder app (Natural Tones / Classic Ivory…) | slow push + drift right (#67→#70 ~8%) | the URL bar is the hero: the domain renders in blue then black | slide down |
| #71–#76 | 3 | CTA | the browser slides down and out as "Gr" blur-types in with a green fringe (#71); "Grab your" → "custom" (grey, ghost, lower) → "custom URLs today" (#72–#74) | locked; #76 the line shifts left ~10% | two-line build; the second line's words arrive ghosted then brighten | cut |
| #77–#84 | 4 | End card | "aistudio.google.com" small, centred, grey | locked | none | end (no logo) |

## 4. Transition inventory
- **Blur-in with chromatic fringe** (#1→#3, #6→#8, #13→#14, #57→#59, #71→#72): text enters out of focus, tinted by the four brand colours, sharpening left to right. It is the one text-arrival state, used everywhere.
- **Glyph scatter → icon assembly** (#3→#6): the letters of "Introducing" break into tumbling strokes, and some strokes become the link glyph. The type literally becomes the feature's icon.
- **Line scale-down + background glow** (#9→#10): the feature name shrinks in place, a sign that it is exiting.
- **Oversize-settle logomark** (#11→#12): the mark enters blurred at ~2.5× and settles to text size, then "Google AI Studio" appends.
- **Tilted window rises** (#16): the only 3D perspective in the film, used for the first UI entrance.
- **Click → push** (#18→#19, #24→#26): each click drives the camera onward. Nothing cuts during the flow.
- **Subtract to one control** (#30→#31): every sibling fades, the survivor grows a glow stroke, then the camera zooms to 4×.
- **Field → button morph** (#42→#44): the input field becomes the button in the same position via a white fill wipe.
- **Button → split-flap pill** (#46→#47): the white face rolls up like a flip-board card to reveal a dark status pill.
- **Status pill slot roll** (#50→#51): the label changes by vertical roll within a fixed container.
- **Pill → squircle → app icon** (#52→#56): the container contracts to a square, a line icon draws, then a colour wipe fills it.
- **Aurora sunrise** (#57→#59): the ground's rainbow rises behind a black horizon. This is the climax.
- **Scale-down into context** (#61→#63): the hero card shrinks into its real place in the UI and pulls back to the full window.
- **Slide-out under type** (#70→#71): the browser drops out the bottom while the CTA types in.

## 5. Easy-to-miss details
- The gradient stroke **rotates hue on every frame** while a field is focused (#33–#38), like a conic gradient spinning ~90° per 0.5 s. That is the "AI is alive" signal, done without sparkles.
- The glow under controls is **offset, not centred**: orange bottom-left under the field (#40), yellow-green under the white bar (#43), orange-red right under the icon (#53–#55). It wanders, so holds are never static.
- "Available" (green) appears only **after** the typing stops (#37), a real validation state delayed ~0.5 s.
- The ".ai.studio" suffix is 40% grey, and **the whole group re-centres** when it arrives (#38→#40), so the frame's centre of mass stays on the slug.
- The camera **pulls back** mid-typing (#36→#37) to make space for the "Available" label and suffix. The zoom is driven by layout need.
- The "Get started" button **stays** while the form scrolls up under it (#25→#26): a sticky element that bridges two screens.
- The rocket line icon tilts between #54 and #55 (a small launch wiggle) before the colour fill replaces it.
- The coral fill enters as a **diagonal curved wipe** (#56), the same curve as the horizon arc that appears next.
- The CTA's second line ("custom URLs today") enters **ghosted and offset down-left** (#73), then slides into alignment and brightens (#74).
- The end card has **no logo**, only the URL, for ~4 s. The brand was front-loaded at #11–#15.

## 6. Pacing curve
Title and brand run for the first 7.5 s (#1–#15), which is unusually long. Then the UI flow runs at ~2–3 s per state (#16–#30), accelerating into macro (#31–#46) where each beat is ~1–2 s. The breath is the loading pills (#47–#52, 3 s of nearly nothing happening, on purpose, to mimic waiting). Climax: the aurora sunrise with "is published" (#57–#61). A proof beat follows (the real browser, #62–#70). Then two quiet cards: CTA 3 s and URL 4 s. The ending subtracts to a URL on black.

## 7. What makes it premium
- One control gets the whole stage. The URL field fills the frame at 4× on pure black. A normal demo would show the form.
- The brand gradient is used only as **light on edges** (stroke + halo). The UI itself stays monochrome, so the colour always means "this is the active/AI thing".
- Each state change is a **morph in place** (field → button → pill → icon). The centre of mass barely moves from #38 to #61.
- A real waiting state is dramatised instead of skipped ("Setting up domain", "Publishing your app").
- The payoff is proven in real browser chrome with the real URL, after all the abstraction.

## 8. Reusable techniques
1. **Glyph-scatter to icon.** Break the title word into individual glyph strokes, rotate them 30–90° and scatter them outwards over ~1 s (ease-out), then pull 2–3 of the strokes into the feature's icon at centre over ~0.5 s. Blur the stragglers.
2. **Hue-rotating focus stroke.** 1.5 px conic-gradient stroke on the one focused control, rotating ~180°/s, plus a 60 px blurred halo in a wandering off-centre position (drift ~10% of the control width per second). Only one control has it at a time.
3. **Chromatic blur-in.** Text from 30 px blur → 0 with a left-to-right focus sweep over ~0.6 s. While blurred, the glyphs are tinted by the brand gradient; they end white.
4. **Field → button → status pill → icon.** Keep the same centre: white fill wipe L→R (0.5 s) turns the field into a button; after the click, a split-flap roll flips it to a dark status pill; labels slot-roll every ~1.5 s; the pill contracts into a squircle (0.5 s), a line icon draws, a colour wipe fills it.
5. **Aurora sunrise payoff.** Black curved horizon in the bottom third; a spectral gradient rises behind it over ~1 s while the confirmation line blur-types. Push 10% during the hold.
6. **Shrink-back to context.** After the macro payoff, scale the hero element down ~3× into its actual location inside the full UI so the viewer sees where it lives, then click through to the real result.
