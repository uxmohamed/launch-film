# Layo — analysis (74 frames, ≈37 s)

## 1. One-line concept
Layo lets businesses build apps that run *inside* AI assistants (ChatGPT, Claude). The spine is a before/after on one identical prompt: "Book me a hotel in New York City" → "Sorry, I can't help with that" (#13–#16) → Layo (build → connect → deploy) → the same prompt now returns a live hotel map app (#54–#63) → "Your app. Right when they need it." → Layo logo. It is framed by a blinking text caret at start and end.

## 2. Visual world
- **Background:** pure white. A single soft gradient "glow" lives in one corner and changes hue per chapter: sky/cyan blue bottom (#11–#22), lavender-blue bottom-right (#31–#36), peach/orange bottom-left (#37–#43), bright blue top-left sweep (#44–#47), blue bottom-right for the logo (#65–#70). The glow is a large blurred radial/curved shape, ~40–60% of the frame, with a crisp-ish curved leading edge (like a light wave).
- **Type:** a clean grotesk (SF/Inter-like), regular weight, small (cap height ~1.5% of frame), near-black. Everything is "typed" with a **blue text caret**. The chapter menu uses the same size in active (dark) vs inactive (light grey ~20% opacity) states.
- **UI staging:** two modes, on purpose. (a) *Third-party context* (ChatGPT) appears in a **real iPhone with black bezel and dynamic island**, cropped by the frame bottom and rising (#11–#16, #56–#63). (b) *Layo's own product* appears as **flat frameless UI panels** at macro crop: the editor window, the chat composer card, the data table, the toolbar with Publish. Shadows are very soft (8–16 px, low opacity).
- **Motifs:** the caret; the "Book me a hotel in New York City" chat bubble; the NYC map with pink pins; the "Crosby Street Hotel" card.

## 3. Shot list
| Frames | ≈s | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1–#3 | 1.5 | Caret | white; blue caret at center (#2), blinks off (#3) | locked | blink ~1 s period | typing starts |
| #4–#6 | 1.5 | Typing | "Your customers" → "just" (#5, newest word in a light blue selection/ghost state) → "…asked AI" | locked | per-word typing; the line stays centered and re-centers as it grows | composer forms |
| #7–#10 | 2 | Composer | "+" icon and send circle fade in on either side → full pill input with soft shadow: "Your customers just asked AI to do your job." | locked; #10 drifts up ~2% | the pill container materializes *around* existing text (#7 ghost, #8 solid); "job." fades in last | cut |
| #11–#16 | 3 | Failure demo | caption "...and you weren't there." top; iPhone rising from the bottom with ChatGPT; blue glow bottom-right | phone rises ~5% then settles | user bubble appears (#13), refusal "Sorry, I can't help with that." (#15) | cut |
| #17–#22 | 3 | Type card | "Be" → "Be the answer." with caret; blue glow bottom | locked | per-word typing with ~1 s hesitation after "Be" (#17–#19); caret persists at the end of the line | cut |
| #23–#25 | 1.5 | Reveal | frameless phone showing the ChatGPT result *with a map*; Layo mark above → "Layo" wordmark (#24) | locked | wordmark writes on beside the mark; the phone UI blurs (~10 px) and fades | pull-out |
| #26–#30 | 2.5 | Editor wide | the full Layo editor window (layers left, phone canvas center, AI chat right) over a giant blurred NYC map; caption "Your app, inside AI." types in above (#27–#28) | slow push ~3–5% | caption words type in, the last word ghosted | cut |
| #31–#33 | 1.5 | Step 1 | left: 3-line chapter menu, "Build the interface." active; right: Layo AI composer card ("Room card 1 ×  Make the room cards clickable to show booking details") | locked | prompt text types in; chips "Create overlay", "Change styling" | card swap |
| #34–#36 | 1.5 | Step 1 result | map card with the "Crosby Street Hotel $960/night" card, blue "Card" selection label | card slides up | the hotel card appears as a selected element; #36 the whole panel slides up ~30% and crops at the top | menu advances |
| #37–#43 | 3.5 | Step 2 | menu scrolls: "Connect your data." active (same y the previous active line occupied); right: "Create a database" table (Title / Description / Image / Price) + AI side panel; peach glow | slow vertical pan up (table rises ~15% over 7 frames) | inactive lines fade to ~20% | chapter change |
| #44–#47 | 2 | Step 3 | "Deploy everywhere" in white over a blue glow top-left; macro crop of the toolbar (Share, **Publish**) and AI chat "Thought for 4s / Your app is ready to go live, want me to publish?" | slide left ~5%, then fade | message text fades (#47) | isolate button |
| #48–#49 | 1 | Button | the "Publish" button alone at center | locked | press: a light sheen sweeps across it (#48), slight scale down ~95% (#49) | morph |
| #50–#53 | 2 | Integrations | button → "ChatGPT" row card with toggle off (#50) → toggle on "Active" (#51) → second row "Claude" (Active) stacks below (#52) | locked | toggle slide + green fill; new row grows the card downward | collapse |
| #54–#55 | 1 | Bubble | the card collapses to a single chat bubble "Book me a hotel in New York City" | slight drift | — | phone forms |
| #56–#59 | 2 | Success demo | iPhone materializes around the bubble (#56 ghosted ~30% → #57 solid); response "Absolutely, here are hotels from Stayspot" + map app | phone rises steadily ~10% | the map renders in | phone exits up |
| #60–#63 | 2 | Tagline | phone moved up and cropped by the frame top, faded at the bottom; "Your app. Right when they need it." types below | continues rising | last words ghost-type | cut |
| #64–#70 | 3.5 | Logo | Layo mark alone (#64) → caret appears (#65) + blue glow sweeps in → "Layo" typed (#66) | locked | caret blinks on/off at 0.5 s frames (#67 off, #68 on, #69 off, #70 on) | clear |
| #71–#74 | 2 | Bookend | white → lone caret (#72) → white | locked | same caret as #2 | end |

## 4. Transition inventory
- **Caret-born text** (#2→#4, #17→#20, #65→#66): every line enters by being typed. The caret is the film's cursor and its narrator.
- **Container materializes around text** (#6→#8): the input field builds itself around a sentence already on screen; text first, UI second.
- **Hard cut on narrative turn** (#10→#11, #16→#17): the problem, then the rallying line.
- **Blur-out of UI into brand** (#23→#25): the result phone blurs as the wordmark writes on.
- **Wide → macro chaptering** (#30→#31): from the whole editor to single-panel crops with a left-hand chapter menu.
- **Chapter-menu scroll** (#36→#37, #43→#44): the active line changes and the list scrolls so the active line holds a fixed position. The right-side content swaps at the same moment, and the corner glow changes hue.
- **Isolate the CTA** (#47→#48): everything around "Publish" disappears, leaving the button alone on white.
- **Button → card → bubble → device morph chain** (#49→#50→#54→#56): pressing Publish *becomes* the integration toggles, which *become* the user's message, which *becomes* the phone. Each step keeps roughly the same screen position and grows or shrinks around the center.
- **Upward exit + caption** (#59→#60): the device keeps rising out of frame while the caption types in the vacated space.
- **Caret bookend** (#70→#72): the film ends on the same element that began it.

## 5. Easy-to-miss details
- The identical prompt text ("Book me a hotel in New York City") in #13 and #54 is the before/after hinge, and the phone framing is identical too (bezel, crop, rise).
- The newest typed word is shown in a lighter/ghost state or a light blue selection tint (#5 "just", #7 "to", #20 "answer", #27 "AI."), then darkens. This is a per-word "arrival" state rather than per-letter typing.
- The hesitation after "Be" (#17–#19: Be, Be|, Be |) makes the typing feel human: ~1 s pause before "the answer."
- The composer pill in #8–#10 has a subtle drop shadow; it drifts up ~10 px in #10 before the cut to prevent a dead hold.
- The ChatGPT phone in the failure shot is cropped at ~50% height. The frame never shows the full device, which keeps UI text legible.
- The chapter menu's inactive lines are ~20% grey, and the active line is swapped, not animated in, so the list reads as a table of contents.
- The corner glow is a different color for each chapter (blue/lavender/peach/blue), a soft chapter code like Figr's palette-per-act.
- The Publish press has a light sweep ("sheen") across the button (#48), then a ~5% scale-down (#49). This is the only "click" feedback in the film, with no cursor ever shown.
- In the logo hold the caret blinks at exactly the frame rate (on/off each 0.5 s), which means a 1 s blink cycle.

## 6. Pacing curve
Quiet caret open (1.5 s) → typed thesis (3.5 s) → problem demo (3 s) → deliberate slow "Be the answer." (3 s) → brand reveal + editor wide (4 s) → three evenly timed chapters (~3 s each, fastest at step 1) → quick morph chain Publish → toggles → bubble → phone (~5 s, the climax of *causality*) → tagline (2 s) → logo with blinking caret (3.5 s) → caret bookend (2 s). The rhythm is even and calm. The climax is the payoff of the repeated prompt, not a speed-up.

## 7. What makes it premium
- A narrative device (identical prompt before/after) instead of a feature list.
- The caret gives every line a consistent entrance and makes the film feel "authored in real time," matching an AI-builder product.
- Strict staging grammar: real iPhone bezel = the *customer's* world (ChatGPT); frameless flat panels = *your* world (Layo editor).
- White space dominates. Color is limited to one wandering corner glow per chapter.
- A continuous morph chain from the CTA button to the outcome shows cause and effect without cuts.

## 8. Reusable techniques
1. **Caret-typed copy with ghost tail.** Blue 2 px caret; append 1 word per 0.25–0.5 s; newest word at ~40% opacity or with a light-blue selection tint, resolving to 100% over 0.3 s. Add one deliberate 1 s hesitation per film.
2. **Text-first container.** Type the sentence bare, then fade/scale the input pill (98%→100%, 0.4 s) with its icons around it.
3. **Before/after on one prompt.** Show the same user message twice in the same device framing: first failing, later succeeding with rich UI.
4. **Sticky-active chapter menu.** A left-column 3-item list; the active item is dark and the rest ~20%. On a chapter change, scroll the list so the new active line lands at the old line's y (0.4 s ease-in-out), and swap the right panel and glow hue simultaneously.
5. **CTA isolate + press.** Remove all context around the key button (0.3 s fade), sweep a sheen across it (0.3 s), scale to 95% and back, then morph the button into the resulting state card.
6. **Morph chain to outcome.** Button → settings card → chat bubble → device: each step keeps the center fixed and changes only the container's size and shape (0.4–0.5 s each).
7. **Device exits up, caption fills the void.** Rise the phone ~10%/s out of the top with a bottom fade mask and type the tagline in the lower third.
8. **Blinking-caret logo + bookend.** Type the wordmark after the mark, blink the caret at a 1 s cycle for ~3 s, then return to a lone caret on white.
