# Perplexity Computer — hybrid compute on the Mac App (138 frames ≈ 69 s)

## 1. One-line concept
Perplexity's "Computer" agent can now split a task between cloud frontier models and a local model on your Mac. The spine is **one real finance task followed from prompt to deliverable**, told as caption → proof → caption → proof. The privacy moment ("PII classifier") sits at the centre: the agent flags sensitive data, then runs it locally.

## 2. Visual world
- **Two grounds, one chapter break.**
  - Act 1 (#1–#28) is near-black with slow diagonal **light streaks**: soft teal, amber and blue bokeh bands at about 30° that drift the whole time. It's a "hardware keynote" look.
  - Act 2 onwards (#29–#138) is a flat **warm charcoal (#1c1b1a-ish)** with no texture. The only light is a faint teal under-glow behind the prompt box (#29–#58).

  The streak world is where hardware lives; the flat world is where software lives.
- **Type:**
  - A **book serif** (Perplexity's editorial face, like FK Roman or Tiempos) at regular weight for all captions: about 4.5% of frame height, two centred lines, off-white.
  - UI type is a small grotesk at about 1.5–2%.
  - Mono is used for the PII field values (#74–#79), with the field labels (EMAIL, PHONE, PERSON, ADDRESS) in a **muted red/orange**. That is the only warm accent in the whole film.
- **Hardware as line art.**
  - The Mac mini (#12–#20) and MacBook (#21–#28) are drawn as dark bodies whose **edges alone catch the light**: rim-lit outlines with an iridescent teal→amber gradient along the bevel.
  - The Mac mini's single power LED is a white dot. It is effectively the film's "atom" for the hardware act.
- **UI staging.**
  - Rebuilt, frameless, and centred on the charcoal ground at about 45% of frame width.
  - The full app window appears **once** (#27–#28, inside the laptop screen). It's used to orient, then dives in.
  - Later, a borderless "window" with traffic-light dots (#104–#115) acts as a document card.
- **Colour logic.**
  - Teal = active or selected (the toggle, the hover ring on a model chip, the "Awaiting 2 subagents" header, the glow).
  - Red/orange = PII.
  - Everything else is greyscale.

## 3. Shot list
| # | Dur | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| 1 | 0.5 s | Ground | Streak field only | static | streaks drift | logomark fades in |
| 2–4 | 1.5 s | Logo | Perplexity asterisk mark, ~7% of frame height, centred | static | mark **shrinks** ~100→80% across #2→#4 (slow recede) | fades out; text appears top-left |
| 5–11 | 3.5 s | Type on ground | "Introducing hybrid compute on / Perplexity [Finder icon] Mac App" | ~5% push-in between #5 (text off-centre and large at top-left) and #6 (centred) — a camera re-frame | per-word **ghost-to-white** reveal ("hybrid" grey at #5; "App" grey at #6). The Finder icon pops in as an inline word at #7 (tiny square → full icon over 1 frame) | text dims (#11) as the camera starts to tilt down |
| 12–13 | 1 s | Hardware reveal | Mac mini enters from the bottom-right, lit face | slide/truck up from below | the lit bevel sweeps across the top face (#13 the white face is fully lit) | settles into a centre-bottom composition |
| 14–20 | 3.5 s | Hardware + caption | Mac mini outline at the lower third; caption above: "Computer can now split a task between / cloud and a local model on your Mac." | very slow push | caption ghost-reveal per word (#14 "can now" grey, #15 "and a" grey). **Rim light travels around the chassis**: a teal edge on the left at #14, amber hotspot at the top-centre at #18, white on the right at #20 | caption fades (#20 dims); mini slides right |
| 21–23 | 1.5 s | Two devices | MacBook enters from the left beside the mini (#21), then the camera re-frames onto the laptop alone (#22–#23) | truck left and push | the laptop's rim light brightens edge by edge; the screen is black glass reflecting streaks | the screen "powers on" |
| 24–26 | 1.5 s | Laptop wide | Dock appears (#24); the screen shows the streak wallpaper | slow push ~5% | cursor sits at the Perplexity dock icon (#25–#26) | click → the app window opens |
| 27–28 | 1 s | Orientation wide (in-device) | App window with "What should we work on?" inside the laptop | push starting | window scales up from the dock (genie-free, simple scale) | **push-through the screen**: the laptop bezel and streaks leave frame; the ground becomes flat charcoal |
| 29–31 | 1.5 s | Macro UI | Prompt card: icon, serif headline "What should we work on?", input "Do anything…", chips "Computer", "Orchestrator" | locked | cursor enters bottom-right (#30), glides to the "Orchestrator" dropdown (#31) | click |
| 32–42 | 5.5 s | Macro UI – menu | Popover: "Hybrid" toggle, Local → "Local model", Cloud → GPT-5.6 Sol / Claude Fable 5 / Claude Opus 5 / Claude Sonnet 5 | **camera re-centres upward** to follow the popover (#33–#34: the headline slides down and crops to "What should w…") | popover grows from a tiny ~20% card (#32) to full (#33) in 1 frame. Cursor → toggle (#35), toggle flips teal (#36), → Local model (#37–#38, checkmark), → Claude Fable 5 (#39–#41) | popover shrinks back toward its anchor (#42 at ~70%), then gone |
| 43–58 | 8 s | Macro UI – typing | Prompt types: "Look at the Meridian files in Documents. Rework the model with their revised projections. Benchmark against comparable deals and then update the IC deck if the returns still clear." | camera re-centres down (#43), then locked with a very slight push (#49→#58) | typing about 6–10 words per 0.5 s; the newest 1–2 words are **ghost grey** (#50 "comparable", #51 "the"). Model label now "Local Model / Claude Fable 5". Cursor travels to send (#55–#56); send button inverts white on press (#56–#58) | whole card dims ~40% (#58), then cut to empty charcoal |
| 59–65 | 3.5 s | Status on ground | "[icon] Inspecting Meridian files locally", then a second row "Checking for sensitive info" | the status block **drifts up** from centre (#59) to the upper third (#62) | **shimmer sweep** L→R across the status text: "files locally" bright at #60, "Checking" bright at #62, "sensitive info" at #64 | the whole block fades to 40% (#65), then out |
| 66–69 | 2 s | Single bar | Pill: "Privacy Gate found personal information in this file. How do you want to handle it?" | locked | **teal shimmer band** crosses the pill L→R (#67 left, #68 centre, #69 right) | the pill **expands downward** into a full dialog card (#70) — morph |
| 70–80 | 5.5 s | Dialog card | File "Meridian_management.pdf · 8 names, 9 titles, 8 emails, 8 phone numbers, 14 others"; options "1 Process on my Mac (Recommended)" / "2 Upload anyway"; "Skip file" | card grows (#70 → #73 ~1.15×), then the **camera tilts down** (#76) to crop the top | the file row expands into a mono PII list with red labels (#73–#75, the list grows downward with a scrollbar). Cursor → option 1 (#78: highlight, checkbox teal); "Skip file" relabels to "**Submit**" (#78); cursor → Submit (#79) and clicks (#80, the whole card dims 40%) | dim, then cut to type |
| 81–86 | 3 s | Type on ground | "Perplexity's PII classifier automatically / flags sensitive information" | static | ghost-word reveal (#81 "sensitive" grey, slightly lower); holds #82–#85 | fade to 30% (#86) |
| 87–91 | 2.5 s | Type on ground | "and runs personal and confidential / data on your Mac." | static | appears whole, no stagger (#87) — the second half of the sentence | hard cut (#92 blank-ish) |
| 92–103 | 6 s | Macro UI – agent status | "Awaiting 2 subagents" (teal); row 1 "Pulling market data from web · Verifying across sources… [Claude Fable 5]"; row 2 "Reviewing files locally · Updating the IC deck… [Local model]"; four meters: CPU 27%, Memory 81%, GPU 98%, Tokens 1555→1602→1629 | slow push ~8% (#93→#103) | header fades in first (#92), then row 1 (#93), then row 2 (#98 ghost → #99 solid), then meters. The model chip on row 1 gets a **teal outline ring** (#94) as a highlight. Shimmer crosses "Verifying across sources" (#101). Meter numbers tick (CPU 27→24→21→20→21, Memory 81→83→84, Tokens 1555→1602→1629); sparklines extend | **scale-out**: the block recedes into a window card with traffic lights (#104–#105) |
| 104–115 | 6 s | Document card (window) | Status rows at the top, then "Done — model reworked, benchmarked, and the IC memo updated." Below that, an answer builds: "The headline… 2.3% MOIC / 18.3% gross IRR…", "Benchmark…", "Two things to watch" bullets. Then two artefact cards: a spreadsheet thumbnail "Meridian-Industrial-Holdings–LBO-Mode…" and a teal deck card "Meridian Industrial Holdings, LLC" | camera **scrolls the content up** inside the fixed card (#109 → #112) | the answer streams in paragraph by paragraph (#107 → #110). The two file cards appear (#112) with the right card highlighted (#113–#114) | whole card dims 50% (#115) → cut |
| 116–123 | 4 s | Type on ground (thesis) | "Frontier models run in the cloud. / Sensitive data stays local." | static | per-word ghost reveal ("the" grey at #116; "data" ghost at #119) | fades (#124) |
| 124–130 | 3.5 s | CTA type | "Now available on / Perplexity [Finder icon] Mac App" | static | ghost reveal. The Finder icon grows from a **small blue square** (#126) to the full icon (#127) — echo of #7 | cut |
| 131 | 0.5 s | Logo | Logomark alone, large (~20% of frame height) | — | pop-in | shrinks and moves left |
| 132–138 | 3.5 s | End card | Mark + "perplexity" wordmark, ~7% of frame height | static | wordmark **wipes in L→R with a soft gradient edge** (#132 "perplexi" with "t" fading); settles by #133; tiny ~3% recede over the hold | end |

## 4. Transition inventory
1. **#4→#5 Logo fade → text in a re-framed position.** Motivation: the brand says "hello" first; the thesis follows.
2. **#11→#12 Tilt/truck down into hardware.** The caption dims while the product rises. Motivated by "on Perplexity Mac App" → here's the Mac.
3. **#20→#21 Truck left to reveal a second device.** The Mac mini stays in frame as the MacBook enters, then the framing gives way to the laptop. This is object carry-over across devices.
4. **#26→#27 Dock click → window opens (cause-driven).** The cursor on the dock icon is the cause.
5. **#28→#29 Push-through the screen.** The window grows until the device bezel leaves frame, and the ground switches from streaks to flat charcoal. This is the **chapter break**: hardware world → software world. Only one push-through in the film.
6. **#32→#33, #41→#42 Popover grow/shrink from its anchor.** Real UI behaviour, slowed to about 0.5 s.
7. **#58→#59 Send → dim → hard cut to status text on empty ground.** The prompt card "leaves" and its status line takes over the frame. It reads as the prompt → pill pattern with the container removed.
8. **#65→#66 Status fades → single pill appears.** Weak (a dissolve) but motivated: the check produced a finding.
9. **#69→#70 Pill → dialog (morph).** The bar extends downward into the card. The same top line persists as the card's title.
10. **#80→#81 Submit click → dim 40% → cut to caption.** A **dim-to-exit** used consistently at #58, #80, #115.
11. **#86→#87 Caption 1 → caption 2 as a hard swap** (the sentence continues across the cut).
12. **#91→#92 Cut to near-empty charcoal; header fades in first.**
13. **#103→#104 Scale-out: the status block becomes the top of a window card.** Pull-back reveal ~0.75×.
14. **#115→#116, #123→#124 Dim → caption.** Pure type rhythm.
15. **#130→#131 CTA → logomark hard cut; #131→#132 mark shrinks left while the wordmark wipes on.**

## 5. Easy-to-miss details
- **Rim light as a travelling highlight** (#14–#20): the teal→amber→white glint runs around the Mac mini's bevel over about 3 s. It's the only motion during a 3.5 s hold, and it replaces a push.
- **Inline app icon as a word.** The Finder icon sits at cap height between "Perplexity" and "Mac App" (#7, #127). At the CTA it's born as a tiny solid blue square before resolving into the icon (#126), a 1-frame "pixel → icon" growth.
- **Ghost word is also offset down**: #81 "sensitive" is about 0.3 em lower and at ~25% opacity. It's a blur/ghost-plus-drop arrival state, applied identically in every caption (#5, #14, #81, #116, #119, #124).
- The popover **pushes the camera**, not vice-versa: at #33 the whole composition shifts about 25% of frame height down so the popover fits. The headline gets cropped ("What should w…"). That frame-edge crop sells "macro".
- "**Skip file**" relabels to "**Submit**" the instant option 1 is ticked (#77→#78). It's a real micro-state, kept.
- The model label in the prompt bar changes from "Orchestrator" to "Local Model / Claude Fable 5" (#40→#43), which proves the menu choice persisted.
- **Model chip highlight**: on the status screen, a teal ring draws around "[Claude Fable 5]" for one beat (#94), then relaxes (#95). A 1-frame emphasis ring rather than a zoom.
- **Meters tick as life**: CPU drifts down 27→20% while GPU sits at 98–99% and Tokens climb in steps of +47 and +27. The numbers wobble rather than rise monotonically, which reads as "live".
- The **teal under-glow** under the prompt card (about 60 px of soft bloom at 1080p) disappears once the prompt is sent. Light = "awaiting input".
- End-card wordmark: a gradient-edge **wipe** (soft, about 1 letter wide), not per-letter.

## 6. Pacing curve
- Slow, even and keynote-like throughout.
- Open: 5 s of logo and type, with 8 s of hardware.
- The densest passage is the menu interaction (#32–#42: four clicks in 5 s).
- Longest shot: 8 s of typing (#43–#58). It's deliberately slow because the prompt *is* the story (the "followed object").
- Breaths come after each proof: #81–#91 (5.5 s of type) and #116–#123 (4 s).
- No climax shout. The emotional peak is the Privacy Gate card (#70–#80), marked only by the red PII labels.
- The ending is three stacked quiet cards (thesis, then "Now available", then logo), totalling 11 s (16% of the runtime). That is a long, calm tail.

## 7. What makes it premium
- The hardware is shown **only by its lit edges**, so the Mac becomes a silhouette that belongs to Perplexity's dark world rather than an Apple product shot.
- The prompt is a **real, long, domain-specific finance instruction** (MOIC, IC deck, comparable deals). The artefacts at the end (LBO model, IC memo) close the loop on exactly what was asked.
- One chapter break (streaks → charcoal) happens *through the device screen*, so the change of world is diegetic.
- The UI keeps its real micro-states (toggle, checkmark, "Skip file → Submit", label persisting, meters ticking) but is paced at about 1 action per 1–1.5 s.
- A serif caption against a grotesk UI gives an editorial "narrator" voice that is distinct from the product voice.

## 8. Reusable techniques
1. **Rim-lit hardware silhouette.** Render the device body at ~5% luminance on a dark streak ground, with only its bevels lit by a gradient (teal→amber→white). Animate the highlight's position around the perimeter over 2–4 s instead of moving the camera. Use it when hardware must appear without becoming a product shot.
2. **Push through the device screen as the chapter break.** Orientation wide inside the laptop (1 s), then a scale ~2.5× over 0.5–1 s until the bezel exits. Cross-fade the ground from the textured wallpaper to the flat UI ground on the last 2 frames.
3. **Dim-to-exit.** At the end of every UI beat, drop the whole composition to 40–60% luminance for 1 frame (~0.5 s) *after* the final click, then hard cut to type. The click → dim → caption cadence reads as "done, now listen".
4. **Status shimmer as progress.** Place status text alone on empty ground and sweep a brightness band L→R across it (~1.5 s per line). Add a second line 1 s later. No spinner.
5. **Pill → dialog morph.** The alert starts as a one-line pill (2 s, with a shimmer band), then extends downward into the full decision card while its top line stays put and becomes the title. Card growth is ~0.5 s ease-out.
6. **Caption / proof alternation for a technical claim.** Caption (3–4 s) → UI proof (5–8 s) → caption continuing the same sentence (the "and runs…" split across a cut) → UI proof → thesis couplet. The thesis couplet is two short parallel lines ("Frontier models run in the cloud. / Sensitive data stays local.").
7. **Pixel-to-icon inline word.** At a CTA, the inline app icon enters as a solid-colour square at 40% of its size, then resolves into the icon on the next frame. It echoes the icon's earlier entrance.
