# Sphinx — AI data scientist (documentary-style launch)

400 frames, about 200 s. The sampling ends exactly at #400 (20 full sheets) on a pull-quote, so **the real ending or end card may be truncated.** Treat the "ending" notes with caution.

## 1. One-line concept
Sphinx is an AI agent for data science, working in notebooks and connecting to Snowflake. It's a founder-narrated documentary. The spine is:
- **History cold open:** the 1707 Scilly naval disaster, caused by bad longitude data (1,400 sailors lost), then "Sixty years later" Captain James Cook navigating the Pacific with better instruments.
- Then the CEO: "Data Science doesn't work that way / Your data may have outliers, missing values, poorly documented schemas".
- Then the product demos, interleaved with interview.
- Then an abstract capability sequence (Explore / Examine / Transform / Build a Model / Validates).
- Then an agentic fraud-investigation demo, security (a keyhole cube: Prompts / Data / Outputs), and a customer testimonial ("Our 2 person team now operates like a team of 20.").

## 2. Visual world
- **Ground.** A dusty maroon, burgundy-brown (about #6E4744), with a soft orange glow bleeding from a lower corner. A faint dot or particle field sits on it, with **hairline construction grids** (thin vertical and horizontal rules at about 10% opacity, sometimes with ruler ticks). A cream (#EFEBE3) alternate is used for "In 1707" and the ship. An orange-to-cream vignette gradient is used for security.
- **Palette.** Maroon, cream and one orange accent. Orange means *signal*: the route trail, the navigation error, anomalies, active nodes and the keyhole cube.
- **Type.** A neutral grotesk (Inter or Söhne-like). Captions are tiny: "In 1707" is about 1.8% of frame height, "Admiral Cloudesley Shovell" 3.5% in two lines at the lower left, and capability labels 3%. Over the interview there's a single **large kinetic caption**, about 12–15% of frame height, in cream.
- **Imagery.** Historic engraved portraits rendered as **stippled dot clouds** (#3–9, #37–46). Antique maps in sepia duotone (#10–16, #47–67). A brass instrument dial redrawn as line art (#17–22). A ship engraving (#23–31). Real 4K interview footage (a warm office with a window and plants, two angles: medium-wide and a 3/4 close). A 3D wireframe "data room" of glowing archival charts (#219–246). A particle network (#248–263). A 3D orange cube (#351–376).
- **UI staging.** Three modes:
  - dark native UI, flat and full frame (#139–163);
  - a light UI window with a rounded bezel-like frame that rises from the bottom, seen in tilted macro (#278–291);
  - a two-panel app (chat + notebook) floating on maroon at about 45% + 45% of frame width (#292–295).
- **Depth.** DOF bokeh on the network nodes (#251–253), and the frame rising over the blurred prompt (#278).

## 3. Shot list
| Frames | ~s | Shot | What happens | Exit |
|---|---|---|---|---|
| #1 | 0.5 | Empty cream | Silence beat. | Grid draws |
| #2 | 0.5 | Type on grid | "In 1707", tiny, centred on a hairline cross grid. | Cut to maroon |
| #3–9 | 3.5 | Stipple portrait | A dotted engraving of Shovell **condenses from sparse dots** (#3 faint → #5 dense) and drifts right about 10% of frame width. The name caption sits at the lower left, with an orange corner glow. | Mosaic zoom |
| #10–11 | 1 | Map, perspective | A tilted map arrives through a **pixel-mosaic blur** (blocks about 3% of frame width) that resolves as the camera levels out. | Settle |
| #12–16 | 2.5 | Map + route | A dashed white route arcs across the Bay of Biscay toward the Channel, with an orange dash trail behind it. A "200 miles" label rides on a solid white segment. A slow push (about 3%). | Cut |
| #17–22 | 3 | Instrument dial | A line-art compass or sextant scale (80–100, "E"). An orange readout line splits into two lines, and the error ticks −0.07° → −0.50°. | Cut to cream |
| #23–31 | 4.5 | Ship flicker | The ship alternates **every frame** between an orange dithered version and a grey engraving, while its position jumps (centre, then right, then left). It exits left at #31. This is stop-motion wreckage. | Type |
| #32–36 | 2.5 | Proof type | "1,256 sailors lost" becomes "1,400 sailors lost" (#33). A hold, then the text scales up about 20% and shifts left (#36). | Cut |
| #37–46 | 5 | Type → portrait | "Sixty years later" over an emerging stipple portrait. Then "Captain James Cook" (#39–44). At #45–46 the portrait **disintegrates into dots** and the camera flies through them. | Mosaic |
| #47–67 | 10.5 | Pacific map | The mosaic resolves to sharp (#47–50) on a slowly rotating (about 8°) and pushing map. A dashed route draws across the Pacific (#51–65). This is the longest calm hold. | Dot portrait |
| #68–70 | 1.5 | **Stipple → footage** | A dot-cloud portrait of the *CEO* (the same treatment as the admirals) crossfades into the real interview footage. | — |
| #70–100 | 15 | Interview | A wide angle. The lower third **types on**: "Rohan" (#71), then "Rohan Kodialam / CEO – Sphinx" (#72). Cut to the close angle at #82. | Cut |
| #101–104 | 2 | Keyword box | A cream box with **corner selection handles** and dotted ruler rules extending sideways. It grows as words append: "Data Sci…", "Data Science doesn't w…", "Data Science doesn't work that way" (it wraps to 2 lines and the box resizes). At #104 it **pans out to the left**. | Pan |
| #105–112 | 4 | Data list | "Your data may have" plus items that appear one per 0.5–1 s with small square bullets on filled cream tags: outliers, missing values, poorly documented schemas. The column re-centres at #111–112. | Cut |
| #113–138 | 13 | Interview | Alternating wide and close. | Cut |
| #139–147 | 4.5 | Product UI (dark) | A pixel-mascot and the prompt "What would you like me to do?". Suggestion chips appear (one, then three at #140, with a pull-back of about 10%). Typing: "Make a linear regression model for X using Y", with a data table chip attached. | Send |
| #148–156 | 4.5 | Agent stream | The prompt **flies to the top right and becomes a chat bubble**. The reasoning text streams in. "Read Data.ipynb", then green diff cells ("import numpy as np…", "Show full diff (84 more lines)"), then "Thought for 2 seconds". The content scrolls upward. | Plot |
| #157–163 | 3.5 | Result | A blurred plot placeholder resolves into a scatter with a regression line (#158). A push of about 1.6× onto the chart (#162). | Cut |
| #164–178 | 7.5 | Interview wide | — | Cut |
| #179–181 | 1.5 | Logo build | Flowing ribbon lines (like wind or water streamlines) sweep and gather into the S-mark on maroon. | Cut |
| #182–184 | 1.5 | Wordmark | "sphinx" plus the mark, small (about 5% of frame height), on an orange gradient. This is at about 45% of runtime. | Cut |
| #185–217 | 16.5 | Interview + kinetic type | Big words appear **behind the speaker's head** (rotoscoped, so he occludes letters): "to sup[er]charge" (#189), "the experts" (#190–194, repositioned from the right half to the left half), "as", "as it[s] own" (#209–210), "AI mo[d]ality" (#211–213). | Tilt-whip |
| #218 | 0.5 | Whip | The interview frame tilts upward with heavy vertical motion blur. | Into the 3D room |
| #219–246 | 14 | Data room | A wireframe box room. Glowing orange-and-cream archival charts float at different depths, and the camera drifts through. Tiny centred captions, each about 2 s with a blur-in: "Seeing patterns", "Understanding distributions", "Finding anomalies" (tiny "anomaly detected" tags), "Identifying relationships". At #241–246 the charts **streak past with motion blur** and the room empties (#247). | Particles |
| #248–259 | 6 | Network | Dots emerge and connect into a constellation. The camera flies through, and the near nodes go to bokeh. Orange edges light up. "Explore", then a **letter-dropout** into "Examine" (#255 "E  re"). | Compress |
| #260–263 | 2 | Lattice cube | The network re-orders into a 3D lattice cube: "Transform". The orange spreads through the nodes. | Collapse |
| #264–269 | 3 | Particle morphs | The cube collapses to a cloud, which becomes a line chart ("Build a Model"), which becomes a dotted ring, which becomes a ring with a checkmark ("Validates"). | Ring → box |
| #270–277 | 4 | Prompt box | The ring gives way to a cream input, "What do you want sphinx to do? / Agent Mode", in the same spot. A long prompt types in about the fraud rate, Snowflake and retraining. There's a blurred field of orange "+" shapes behind it. | Rise |
| #278–291 | 7 | Tilted macro app | A light app frame **rises from the bottom and swallows the prompt**, which becomes the first chat message. Then a slow tilted scroll: plan text, "Sphinx added a new cell", code, "Successfully ran a cell", findings ("45,283 rows… 42.3%…"). | Pull back |
| #292–305 | 7 | Two-panel app | Chat plus notebook floating on maroon, then a macro of the code, then the result chart (a pink/yellow fraud spike), held with a push. | Cut |
| #306–320 | 7.5 | Lattice build | A single centred dot stretches into a line, splits into dots, unfolds into diamond lattices, and then fills a wide lattice band. Orange nodes light up progressively (a spreading activation), and the band shrinks at #320. | Cut |
| #321–347 | 13.5 | Interview | — | Cut |
| #348–359 | 6 | Lattice → cube | A macro of the lattice columns, then the lattice plane rotates in 3D over cream, and its tiles **flip into orange cubelets**. They assemble into a cube, and the cubelets slide to form a **keyhole** (#356–359). | Hold |
| #360–376 | 8.5 | Security slot | The keyhole cube turns slowly (about 15° over 8 s). A slot word to its right blurs in and out: "Prompts", then "Data", then "Outputs" (about 2 s each, with a dissolve between). | Slit reveal |
| #377–393 | 8.5 | Testimonial | The customer's webcam video opens **from a narrow vertical slit** (blurred) into a card with corner handles, ruler ticks and an audio waveform at its sides. A lower third reads "Jeff Feng / Chief Data Officer…", with a per-word subtitle strip. | Recede |
| #394–400 | 3.5 | Pull-quote | The card recedes and blurs. "Our 2 person / team / now operates / like a team / of 20." is appended phrase by phrase, centred, at about 5% of frame height. | (truncated) |

## 4. Transition inventory
- **Stipple condense / disintegrate** (#3, #45–46, #68). Portraits form from, and dissolve into, the particle field. The dot is the film's **atom**. It becomes the network, the lattice, the chart, the ring and the cube.
- **Mosaic resolve** (#10, #47–50). A pixel-block blur sharpens as the camera settles. It's the inverse of a pixelate dissolve, and it's motivated as "data coming into focus".
- **Follow the dashed route** (#12–16, #51–65), the historic analogue of a data trace.
- **Frame-flicker between two renderings** (#23–31), an engraving versus an orange dither.
- **Particle → footage crossfade** (#68–70). This carries the historic dot-portrait language onto the real CEO. It's the film's central match: *explorers → today's data experts*.
- **Pan-off** (#104): the keyword box slides out left while the next header is already there.
- **Prompt → bubble** (#148) and **prompt swallowed by a rising window** (#278). Both are object lineage.
- **Tilt-whip out of footage** (#218) into the 3D space.
- **Motion-blur fly-past** (#241–246) empties the room into a void, and the network grows from it.
- **Particle morph chain** (#259–270): network, cube, cloud, chart, ring, check, prompt box. The *verbs* (Explore … Validates) are rendered as shapes.
- **Dot → line → lattice unfold** (#306–310), a line-to-structure build.
- **Lattice → cube assembly** (#350–359). The flat data structure becomes a secure object.
- **Slit reveal** (#377) for the testimonial video.
- **Recede + blur under a quote** (#394–395).
- There are many plain hard cuts to and from the interview, with no carrier. The interview works as the "home base".

## 5. Easy-to-miss details
- The CEO is introduced with the *same stipple treatment* as the admirals (#68). It's a one-second rhyme that frames him as the next navigator.
- The lower third types on letter by letter ("Rohan", then the full name), not by fade (#71–72).
- The kinetic caption is composited behind the speaker. His head occludes letters mid-word (#189, #210, #212), and the caption jumps from the right half to the left half between phrases (#190 → #191).
- The error readout's orange line **doubles** as the error grows (#19 → #20). The magnitude is shown by the stroke count.
- The number ticks only once (1,256 → 1,400), then the type scales about 20%. That's emphasis by scale, not by colour.
- The capability captions blur in letter-group by letter-group ("Undec…" at #228).
- Tiny "anomaly detected" labels float on the charts (#232–235). They're easy to miss and pure texture.
- Orange spreading through the lattice (#312–319) reads as "the agent working" without a spinner.
- The testimonial frame carries a waveform at its edge that pulses with speech (#381–390).

## 6. Pacing curve
- A very slow, essay-like open. The history act runs about 34 s with holds up to 10.5 s (the Pacific map), and there's no product for 70 s.
- Then a steady alternation: interview (7–16 s) → a graphic or demo insert (4–15 s) → interview. The interview makes up roughly 45% of the sampled runtime.
- The logo arrives mid-film (about 45%) as a 3 s punctuation.
- The densest, fastest passage is the abstract capability run (#219–270, about 25 s, a new shape every 1–3 s), followed by the long agentic demo (#270–305, about 18 s).
- The late act moves security (8.5 s), then social proof (8.5 s), then the pull-quote. It closes on proof rather than on the product.

## 7. What makes it premium
- It borrows documentary grammar: a historical parable with a precise date, names and casualty count. The graphic system (stipple, maps, instruments, ruler hairlines) is derived from the parable, then reused for the modern product.
- One particle atom does the portraits, the data, the network, the lattice and the logo, so a 200 s film with 10+ interview cuts still feels like one world.
- Restraint in colour: orange only ever marks signal (the route, the error, anomalies, active nodes, the secure cube).
- Real, specific demo content (a fraud rate of 42.3%, 45,283 rows, Snowflake) rather than a generic "analyze my data".

## 8. Reusable techniques
1. **Historical parable open.** "In [year]" (tiny, on a grid), then a stippled portrait with the name at the lower left, a map with a dashed route, an instrument readout of the error, and a casualty number. Take 30–35 s. Then match-cut the parable's rendering onto the founder.
2. **Stipple portrait condense.** Dots scatter at 0% density, then reach the full portrait over 1–1.5 s while drifting 10% sideways. Reverse it for the exit, with a push through the dots.
3. **Mosaic-resolve arrival.** Start the image as 3%-wide pixel blocks with a perspective tilt, and resolve to sharp over 1.5–2 s as the camera levels out.
4. **Caption behind the speaker.** One or two words at 12–15% of frame height, cream, composited behind the rotoscoped head. The phrase changes about every 1 s, and the side alternates.
5. **Verb-shape morph chain.** One particle system becomes a new shape for each verb (network → cube → cloud → line chart → ring → check). Each station gets 1.5–3 s with a one-word caption. The last shape morphs into the product input box.
6. **Prompt swallowed by the app.** A floating prompt card types in. Then the product window rises from the bottom edge (about 0.8 s, ease-out), the card docks as message #1, and the camera tilts about 8° to scroll the agent log.
7. **Slot word beside a hero object.** The hero object turns slowly and one word to its right cycles every 2 s with a blur dissolve.
8. **Slit-open testimonial.** Customer footage opens from a 5%-wide vertical slit into a handle-cornered card over 0.5 s. Then word-level subtitles, then it recedes and blurs under a big pull-quote.
