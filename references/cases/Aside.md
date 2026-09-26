# Aside — agentic browser launch (176 frames ≈ 88 s)

## 1. One-line concept
Aside is a local-first AI browser agent that actually completes long web tasks; the spine is "We killed [other AI apps] → they promised to do the work but bury you in buttons and stop when it gets real → Introducing Aside → watch it cancel subscriptions end-to-end → benchmark → anything you can do in a browser → private/local → BYO subscription → aside.com". A rant-then-proof structure delivered as kinetic type that literally lives inside UI chrome.

## 2. Visual world
- **Two palettes, used as acts:** Act 1 "the problem" and Act 3 "claims" on near-black charcoal (#262626) with white type; Act 2 "the demo" on pure white with dark grey text; the logo reveal is a blue vertical-streak gradient (like light through blinds / motion-smeared glass).
- **Type:** one geometric-ish grotesk (Inter Display / Suisse-like), medium weight, set LARGE — hero phrases 8–10% of frame height, always centred. Accent colour: a single cyan-blue (#1E9BE0) used on the word currently being spoken (#4 "kill", #11 "promised", #12 "work", #14 "Instead,") and on the Aside benchmark bar. A lavender variant on "gets" (#25).
- **Icons as words:** line-icons from the product (globe, key, lock, eye, server, message) are inserted inline in sentences at cap height ("across 🌐 websites", "runs ▭ locally", "🔒 private"). The type system and the UI icon set are one language.
- **UI staging:** product UI is shown as native-scale, flat, shadowless-or-soft-shadow components cropped macro — a search/Ask bar, a chat bubble, an activity timeline — never a full window except #52–#54 and a MacBook mock (#143–#146). The rest of the time the "screen" is just white space and the UI component floats in it.
- **Competitor iconography:** rival app icons (rounded-square 3D-glossy tiles) are dropped into a macOS-dock-like tray and a trash can — satirical but stylised.

## 3. Shot list
| Frames | ~Dur | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–#3 | 1.5 s | Search bar tiny | small dark "Search for…" pill, Search / Ask AI buttons | fast push-in ~3× by #3 | I-beam cursor appears | continued push; bar fills frame |
| #4–#9 | 3 s | Type in bar | "We kill" → "We killed" typed in the bar, then three app icons slide in from right pushing text left | bar is now frame-wide; horizontal truck left | letters appear in accent blue then settle to white; icons enter with ~10% overshoot | bar dissolves, icons shrink up |
| #10–#13 | 2 s | Trash | icons (small, top) → "They promised us to do the work"; one icon drops into a trash-can glyph | locked | per-word colour highlight; icon falls into bin | bin morphs into a dock |
| #14–#17 | 2 s | Dock | "Instead, they bury you in"; dock grows 2→4 icons; cursor clicks an AI app | locked | dock width expands per icon; click pops "Connect App +" button | button clones |
| #18–#19 | 1 s | Button storm | dozens of "Connect App +" buttons at different depths, motion-blurred | fast pan up | chaotic duplication | cut to "bu" |
| #20–#24 | 2.5 s | Type | "buttons…" → "Then" | locked | typewriter per letter (#19 "bu"), ellipsis dots appear one by one | a dark card slides in from right |
| #25–#27 | 1.5 s | Card | "Then," pushed left by chat-input card containing "they stop when it gets real" | truck | card enters from right edge, text inside types | "Then," exits left; card becomes an input |
| #28–#34 | 3.5 s | Chat | Ask AI input; user bubble "Why did you stop?"; AI refusals stack: "I can't do that", "Please approve action", "I can't sign in…", "I can't do sensitive tasks" | slight push-out to show dock under | refusals stack one per 0.5 s pushing upward | cursor drags the AI icon out of the dock |
| #35–#36 | 1 s | Trash physics | refusal chips crumple/tumble and fall into the trash icon with the dragged app | locked | chips rotate ~70°, fall with gravity | dock remains |
| #37–#39 | 1.5 s | Introducing | "Int" → "Introducing"; new app icon in dock; cursor clicks it; icon genie-expands upward like macOS window-open | locked | genie warp: icon trapezoid stretches to fill frame | fills with blue gradient |
| #40–#43 | 2 s | Logo | "Aside" in large translucent white over blue vertical light streaks | push-in ~1.1× | gradient brightens/desaturates to grey-white #43 | flash to white |
| #44–#51 | 4 s | Claim on sidebar | "A browser that gets complex work done" → "across 🌐 websites 🔑 accounts 🕘 history" beside a ghosted browser sidebar | slow pull-back | lines appear grey then ink to black (#46→#47); staggered right-aligned list | sidebar fills in with real UI |
| #52–#54 | 1.5 s | Full window | Aside new-tab page with task cards | pull-back to full window | UI resolves from ghost | push into the Ask bar |
| #55–#60 | 3 s | Prompt | Ask bar isolated; cursor clicks, types "cancel all unused subscriptions and request refunds" | locked, slight push | typewriter ~8 chars/frame | bar becomes user bubble |
| #61–#64 | 2 s | Chat | user bubble top-right; agent reply types in; everything dims (#64) | locked | streamed text with blue shimmer on newest words | dim to 30% |
| #65–#67 | 1.5 s | Status | "⏱ searching browsing history for" (status line enlarged to headline) | locked | shimmer sweep left→right across text | fades grey |
| #68–#73 | 3 s | Accordion | "Credit card ⌄" headline → click → chevron flips, list of sources expands (Chase card overview, MEMORY.md, passkey) | pull-back & drift up | text scales from ~12% frame to ~5%; list rows stagger 2 frames | scroll up |
| #74–#85 | 6 s | Timeline scroll | vertical activity timeline with blue progress dot on a thin rail: open bank site (full screenshot card), sign in with passkey, open statement, "You paid for Netflix, Amazon Prime, LinkedIn Premium…" | continuous vertical scroll ~ constant speed | blue dot travels down the rail ahead of content | rail becomes horizontal line |
| #86–#91 | 3 s | Branch | line with dot → "Spawning subagents in parallel" in a rounded bracket node; camera trucks along | truck right | text types, box draws | line branches into 3 |
| #92–#97 | 3 s | Subagents | 3 rows "Spawned subagent · LinkedIn/Netflix/Amazon"; push into LinkedIn row until icons are huge | push-in ~4× | rows appear stagger 0.25 s | "Inspecting…" |
| #98–#103 | 3 s | Result | "You didn't use LinkedIn… I'll ask for a refund" → "Starting a chat with support" → "Asking for a refund" → "Your $120 refund…" | scroll up | steps append one per 0.5 s | cut to chat |
| #104–#107 | 2 s | Punchline chat | user: "Dammm, how did you just do that?"; agent: "Because I'm a frontier browser agent… Have a look!" | locked | typing | a black circle appears on the word and grows |
| #107–#109 | 1 s | Circle wipe | dark circle expands to fill → a glowing blue bar shoots in from left | — | circle wipe ~4 frames | bar becomes chart |
| #110–#115 | 3 s | Benchmark | horizontal bar chart: Aside 99% (glowing blue), Browser use 97%, GPT 5.4 92%, Claude 86%, ChatGPT Atlas 70% | slow pull-back | bars grow from left; glow bloom on hero bar; title added #111 | cut |
| #116–#121 | 3 s | Claim | "Anything you can do in a 🌐 browser" | locked | word-by-word, lines added below; then all but "🌐 browser" removed | "browser" swapped to logo |
| #122–#131 | 5 s | Slot list | "Aside can do it for you" → "can do → sign in / messaging / video play / presentation" with a grey list scrolling beneath (next options visible at 25%) | locked, sentence shifts left as options widen | vertical slot-reel; icon swaps with word | icon isolates |
| #132–#134 | 1.5 s | Icon zoom | presentation icon grows to fill ~60% frame | push-in ~6× | — | hard cut to white |
| #135–#142 | 4 s | Privacy claim (white) | "everything is private under your…" → "Data never leaves your device"; words split apart to make room for a lock icon (#138–#139) | locked | words physically separate horizontally then icon drops in | laptop rises from bottom |
| #143–#146 | 2 s | Device | MacBook with Aside UI → lid flips to closed/top view (#145) | rotation ~90° | laptop-lid close as a flip | shrink out |
| #147–#150 | 2 s | Claim | "Everything runs ▭ locally, encrypted" with typing glitch "encrypt$T" (scramble) | locked | words part to insert icon; scramble text | cut |
| #151–#159 | 4.5 s | Password field | "Aside won't let AI read_your_passwords" → text becomes a password input; cursor clicks eye icon → turns to asterisks, asterisks shrink | truck right | text→field morph; masking | eye icon remains, bg flips black |
| #160–#167 | 3.5 s | BYO | eye-off icon → "Bring your own 🔑 subscription" → row of model logos scrolling left into Aside icon | truck left | icon carousel | Aside icon alone |
| #168–#176 | 4.5 s | End | "Aside a browser that does your work" → "your asi work" (logo name emerges between words fading out) → "aside.com" | locked | per-word; the middle morph | hold ~1.5 s |

## 4. Transition inventory
- **Push-in to container** #1→#4: tiny UI bar grows until it's the stage for type.
- **Object pushes text** #5→#7, #25: incoming element shoves the previous words off frame.
- **Cursor-driven** #16, #34, #38, #156: clicks and drags motivate every state change in the rant.
- **Genie/app-open warp** #38→#40: macOS window-open used as the logo reveal.
- **Whiteout** #43→#44 and #134→#135: act changes.
- **Line-carries-camera** #85→#92: the timeline rail becomes the bracket line that branches into subagents.
- **Circle wipe from a word** #106→#108: black dot appears on "Have a look!" and swallows the frame (dark mode for data).
- **Text→UI morph** #153→#157: "read_your_passwords" becomes a password field.
- **Icon-scale cut** #132→#134: icon balloons, then hard cut.
- **Name emerges from sentence** #172→#173: "your [asi] work" — outer words fade to 20%, brand appears between.

## 5. Easy-to-miss details
- Active word in accent blue then desaturates to white ~0.5 s later — a karaoke highlight that tracks VO.
- Blue shimmer (gradient sweep) on streaming agent text and status lines (#62, #65) — mimics product's "thinking" state.
- Soft outer glow on the dark-mode search bar (#4–#9) ~20px cyan halo at 15% opacity.
- The progress dot on the timeline rail (#74–#91) leads the scroll by ~100px, pulling the eye downward.
- Headings from UI are scaled to headline size then shrunk back to UI size as the camera pulls out (#68→#73) — "UI label as title card".
- Refusal chips fall with slight rotation and clustering, i.e. real 2D physics, not a fade (#35–#36).
- Slot-reel shows the next 3 options at ~25% opacity below, so the list's breadth is felt even though only one is read.
- Glitch "encrypt$T" = character scramble during type-on (encryption pun).
- Asterisks count shrinks 15→9 between #157 and #158 — the field "settles".

## 6. Pacing curve
Very fast, comedic first 20 s (a new beat every ~1 s, lots of cursor slapstick). Logo lands at ~20 s with a 2 s breath. Demo section (~22–55 s) is steady and continuous — no cuts, just one long scroll/truck, giving a "one-take" feeling that proves the agent works end-to-end. Benchmark at ~55 s is the climax (dark, glowing). Final 30 s speeds back up into claim-per-2 s rhythm, ending on a quiet URL hold of ~1.5 s.

## 7. What makes it premium
- The UI's own components (search bar, chat, timeline rail, password field, icon set) ARE the motion graphics; no separate "graphic language".
- One-take demo: the timeline rail carries the camera through 30 s of agent actions without a single cut.
- Discipline: one accent colour, one type family, icons inline with type.
- Satire is animated with physics and cursor acting, not with extra illustration.

## 8. Reusable techniques
1. **UI bar as title stage** — start with the real input at ~15% width, push in 4× over 1.5 s (ease-in-out), then type the headline into it.
2. **Karaoke accent** — current word in accent colour, fades to base colour over 12 frames after the next word appears.
3. **Inline icon words** — replace nouns with icon+word at cap-height; when introducing, split surrounding words apart (~1 em gap, 8 frames) and drop icon in.
4. **Rail-led one-take** — a 2px vertical rail with a glowing dot leading the scroll; content cards append on the rail; constant scroll speed ~120 px/s at 1080p.
5. **Slot-reel list** — "can do ___": the variable word rolls vertically every ~0.8 s; next 3 options visible at 25% below.
6. **Word-spawned circle wipe** — a dot appears at the end of a line and scales to cover (4–6 frames, ease-in) to switch light→dark.
7. **Text becomes field** — a snake_case phrase gains a field outline + eye icon; clicking converts characters to asterisks.
8. **Brand emerges between words** — last sentence; outer words fade to 20% and the brand name types in the gap, then collapses to URL.
