# Cosmos — "more context" feature teaser (41 frames ≈ 20 s)

## 1. One-line concept
Cosmos (visual-inspiration/curation app, cosmos.so) announces that every saved element now carries credits/context (artist, year, location, object, brand). Spine: a single question "What if we had more context?" → the metadata words interleave with images → each image gets a caption → shown in the phone app → "Now live on cosmos.so" → wordmark.

## 2. Visual world
- **Background:** flat warm off-white (#F4F2EF) throughout, no texture, no gradient, no shadows. Gallery-wall neutrality.
- **Type:** neo-grotesk (Helvetica Now / Neue Haas-like), black, tiny — body copy ~1.8–2% of frame height, set like museum wall labels. Caption labels ~1.2%. The wordmark "COSMOS®" in wide caps at only ~4% of frame height. Nothing is ever large except the images.
- **Two-weight trick:** captions mix regular labels ("Redirect Chair by", "Photo by") with semibold values ("Earshot Studios", "A. Snyder") — the field/value structure of metadata is shown typographically.
- **Imagery:** curated editorial photography (chrome chair, black couture gown, Blossfeldt plant photogravure, pearl jewelry, minimalist interior) — desaturated, muted, all very "Cosmos taste". Images are flat rectangles, no corner radius, no shadow.
- **UI staging:** an iPhone screen as a bare dark screen crop (no bezel hardware), floating on the off-white, small (~35% frame height), later slightly larger (~55% crop from top edge).

## 3. Shot list
| Frames | ~Dur | Shot | On screen | Camera | Element animation | Exit |
|---|---|---|---|---|---|---|
| #1 | 0.5 s | Empty | off-white | — | — | — |
| #2–#5 | 2 s | Type | "What if" → "What if we had" → "What if we had more context ?" | locked | per-word; each word arrives with slight baseline offset (#2 "if" lower, #5 "?" lower) and settles — small vertical rise ~4px | first half slides off left, "more context ?" re-centres (#6) |
| #6–#7 | 1 s | Re-centre | "more context ?" centred, then "?" drops | horizontal shift ~ −25% frame | the sentence re-centres on the key phrase, then the question mark is removed (question → statement) | words split apart, images slot in |
| #8–#12 | 2.5 s | Interleave | row: Artist · [image] · Year · [image] · Location · [chair] · Object · [plant] · Brand · [image] · & more | row widens from centre outward; slight pull-back | images pop in between words overlapping them; words are partially covered by images (collage z-order); central chair image is largest and brightens | push into chair image |
| #13–#16 | 2 s | Captioned image | chair image cropped from top; caption "Redirect Chair by Earshot Studios (2024) / Photo by A. Snyder" types in under | locked, image slightly scales | caption values blur/resolve in (#14 "A. Snyder" blurred → #15 sharp) | cut |
| #17 | 0.5 s | Captioned image | black gown, "The Noir Gown shown by Tracy Jones during Paris Fashion Week (2016)" | locked | — | hard cut |
| #18 | 0.5 s | Captioned image | Blossfeldt plant, "Photograph from Urformen der Kunst (1928) by Karl Blossfeldt" | locked | — | hard cut |
| #19–#20 | 1 s | Captioned image | interior, "The OOAA Arquitectura Studio in Madrid, Spain. Designed by Iker Ochotorena"; app action row (share, +, …) appears below | slight pull-back | action buttons pop in | the whole group shrinks into a phone screen |
| #21–#25 | 2.5 s | Phone detail | phone screen with same image + caption + buttons; cursor-dot taps "Iker Ochotorena" | pushes in: phone ~35% → ~55% frame | tap indicator: grey circle on the name (#24) | tap navigates |
| #26–#31 | 3 s | Phone grid | search page "Iker Ochotorena" with Elements/Clusters/Humans tabs; masonry grid of the designer's interiors fills in | pull-back from #26 crop | grid tiles load staggered (#27 three tiles → #28 six) and scroll up | fade to empty |
| #32–#36 | 2.5 s | Type | "Now live" → "Now live on" → "Now live on cosmos.so" (url in a lighter/smaller weight) | locked | per-word, same baseline-settle as opener | cross-fade |
| #37–#41 | 2.5 s | Logo | "COSMOS®" small, centre | locked | appears, holds ~2 s | end |

## 4. Transition inventory
- **Sentence re-centre** #5→#6: rather than cutting, the sentence slides so the key noun phrase becomes the new centre — focusing by layout.
- **Word-split insertion** #7→#8: the key phrase is replaced by its category words, which spread apart and images drop into the gaps.
- **Push into the hero item** #12→#13: the centre image of the row scales up and becomes the next shot.
- **Hard cuts on rhythm** #16→#17→#18→#19: one image per ~0.5 s, identical layout (image top, 2-line caption centred below) so cuts read as a slideshow flip.
- **Shrink-to-device** #20→#21: the "flat" layout is revealed to be the app screen by scaling it down into a phone.
- **Tap-navigate** #24→#26: in-app navigation acts as the cut.

## 5. Easy-to-miss details
- Words enter with a small downward-offset then settle to baseline (#2 "if", #3 "had", #5 "?", #32 "live", #34 "cosmos.so") — a ~3–5px rise over ~4 frames, very subtle.
- Images in the interleave row overlap their neighbouring words (e.g. "Loc[chair]tion"), deliberately obscuring labels — collage, not grid.
- Caption values resolve from blur (#14) — ~4px Gaussian → 0 over 2 frames — while labels are instantly sharp.
- The caption layout in the flat shots is exactly the in-app caption layout, so the shrink to phone is seamless.
- The tap indicator is a soft grey dot, not an arrow cursor — mobile idiom.
- Logo is not animated at all; it just appears and holds 2 s.

## 6. Pacing curve
Slow open (1 word per 0.5 s), acceleration in the interleave (row grows every frame), fastest in the caption slideshow (0.5 s per image), a moderate in-app demo (5 s), then the same slow type for the CTA and a 2 s static logo. Symmetric bookends: type-only open and close on the same off-white.

## 7. What makes it premium
- Radical restraint: tiny type, one background, zero decoration, no shadows — lets the curated images carry the brand's taste.
- The feature (metadata/credits) is demonstrated through typography itself (label/value weights), not explained.
- The content choices (Blossfeldt, couture, design objects) are the brand message.

## 8. Reusable techniques
1. **Baseline-settle word reveal** — each word appears ~4px low at 0→100% opacity and rises to baseline in 4–6 frames (ease-out); 0.4–0.5 s between words.
2. **Re-centre on the key phrase** — after the full sentence lands, slide it horizontally so the key phrase is centred and drop the rest; 8–10 frames ease-in-out.
3. **Word/image interleave row** — category words spaced along a line, images pop into the gaps at varying sizes (hero centre ~1.3× others), overlapping words; row grows symmetrically outward.
4. **Caption slideshow** — fixed layout (image top-centre, 2-line label below), hard-cut every 12–15 frames; values blur-in, labels static.
5. **Flat-to-device shrink** — a full-frame layout scales down to become the phone screen content (0.6× in 10 frames), then push in on the device.
