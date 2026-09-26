# Crosscut C — Harvey, Cloudflare, Firecrawl

Durations at ~2 fps: Harvey 121 frames ≈ 60 s; Cloudflare 111 ≈ 55 s; Firecrawl 133 ≈ 66 s.

## Recurring patterns
1. **One brand-native "atom" carries the whole film.** Harvey: the black dot in a cube/aperture, kept at frame centre. Cloudflare: the selection-handled node plus the sunrise glow. Firecrawl: the orange square pixel. In all three the atom shows up in the intro, in transitions, in UI emphasis *and* in the logo resolve. None of the films relies on a generic transition library; each transition is made from the atom (Harvey collage explode, Cloudflare zoom-through-arrow, Firecrawl pixel dither/staircase wipe).
2. **A persistent ground plate.** Harvey: fibre paper. Cloudflare: orange with scanlines, or a cream dot grid. Firecrawl: a white modular grid. UI never sits on a void: it's always placed on the art world's surface. Harvey's UI keeps ~10–20% of the collage visible around its window. Firecrawl's UI sits in ~70–80% empty grid.
3. **UI is deconstructed, not screen-recorded.** Hub/spoke chips (Harvey), node diagrams (Cloudflare), single cards and JSON (Firecrawl). Full app windows appear only 2–3 times per film, for ≤5 s each.
4. **Moving numbers as proof.** Cloudflare 11→16→20%, instances, updates 31→40. Firecrawl "1,000,000" decoded from dither, and prices. Harvey is the exception (no numbers at all; see contradictions).
5. **Emphasis by colour state change, not scale.** Firecrawl's selected price chip inverts to orange. Harvey's cube faces re-tint pink/teal when "activated". Cloudflare's "localhost" (pale) vs "global" (saturated).
6. **Staggered one-beat reveals of sibling labels.** Harvey pills are ~0.5 s apart (#54–56). Firecrawl extraction tags are ~0.5 s apart (#31–33). Cloudflare headline words add ~0.5 s apart (#9–12). Sibling stagger clusters around **0.4–0.5 s**, slower than typical UI animation (50–100 ms). Film staggers are "readable" staggers.
7. **Scale-down-into-a-card / push-into-a-cell** as the section connector: Cloudflare #31→32, #71→72, #73→77; Firecrawl #101–109; Harvey #88→89 (ellipse into square). Scenes nest inside each other instead of cutting.
8. **Endings by subtraction.** All three strip their world before the logo. Harvey goes from dark cube → paper with just the H. Cloudflare drains orange → cream, with the outline logo then the URL. Firecrawl removes the grid → pure white. End-card holds are long: **Harvey ~1.5–2 s, Cloudflare ~5.5 s (URL), Firecrawl ~5 s**.

## Contradictions (and why)
- **Handmade vs. digital texture.** Harvey is entirely analogue (charcoal, torn paper, animated on twos). Cloudflare and Firecrawl are vector-precise with *digital* texture (scanlines, dither, pixel mosaics). Harvey's audience (lawyers) is sold on judgement and craft. The dev-infra brands are sold on precision and scale.
- **Words.** Cloudflare is copy-led (6+ headline statements, word-by-word). Harvey uses 2 words total ("Intelligence.", "H"). Firecrawl uses 0 headlines, just UI plus one stat. Cloudflare has to explain a platform, while the other two can show one behaviour repeatedly.
- **Cuts vs. continuity.** Harvey uses hard cuts every 2–4 s held together by the centred anchor. Cloudflare pursues one-take continuity (zoom-through, pan along wires, card shrink). Firecrawl mixes both: transformations inside shots, hard cuts between use cases. Rule of thumb: continuity when the story is "one system", cuts plus an anchor when the story is "many facets of one idea".
- **Frame-rate texture.** Harvey deliberately mixes stop-motion replacement (low fps) with smooth camera moves. The other two run smooth throughout, and Firecrawl uses its one-frame flash (#64) as its only rhythmic rupture.
- **Logo scale.** Harvey's end mark is tiny (~5% of frame height). Cloudflare ends on a URL, not the logo. Firecrawl uses a mid-size wordmark (~5% height, ~20% width). None ends on a big logo slam.

## Numbers / ranges inferred
| Parameter | Range observed |
|---|---|
| Shot/beat length, montage sections | 1–2 s (Cloudflare #59–68; Harvey #65–73) |
| Shot length, "reading" beats (UI with text) | 2.5–5 s (Harvey UI windows 2.5–5 s; Firecrawl paper deck 4 s) |
| Clean title hold | "Intelligence." 1.5 s; "1,000,000" ~1 s; "Build without boundaries." ~4 s |
| End card hold | 1.5–5.5 s |
| Sibling label stagger | 0.4–0.5 s |
| Number ticker | 3–4 discrete steps over ~1 s, decelerating |
| Scramble/decode duration | 1–2 s (3–4 sampled frames) |
| Zoom-through factor | ~10–12× over ~1–1.5 s (Cloudflare CTA) |
| Push-in during holds | +5–15% over 2–3 s (Harvey hubs, Cloudflare logo bar, Firecrawl walls) |
| Card-shrink target | ~45–50% of frame width |
| UI window size, full-app shots | 70–80% of frame width, never full-bleed except macro crops (~180%) |
| Standalone UI card size | 25–40% of frame width (Firecrawl chat/product/login) |
| Context dimming | ~50% luminance on neighbours |
| Dither / pixel sweep | band ~30% of frame width, 0.6–0.8 s crossing |
| Rotation during reveal | cubes ~30° flat→3D (Harvey #62–63); Firecrawl fold-up ~60°; Cloudflare chat bubble −8° settle |
| Colour count | 1 brand hue + neutrals in all three (Harvey adds muted mauve/lavender/sage at low saturation) |
