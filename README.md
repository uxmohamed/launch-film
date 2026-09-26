# launch-film

A [Claude Code](https://claude.com/claude-code) skill that makes product launch videos at the level of top studio work, from concept and storyboard to animation and render.

It's built from a frame-by-frame study of **59 real launch films**: product launches, brand films, model announcements, hardware spots and founder documentaries. It doesn't copy any one film. It captures the system behind them, so every new film feels like the same team made it.

## Install

```bash
git clone https://github.com/uxmohamed/launch-film ~/.claude/skills/launch-film
```

## Use

Ask Claude Code something like:

- *"Make a launch video for https://example.com using the site's assets, copy and style."*
- *"Storyboard a 30-second teaser for our new search feature."*
- *"Critique this launch video against the playbook."*

Or call it directly with `/launch-film`.

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | The manual: philosophy, 13 universal laws, workflow, QC checklist |
| `references/modes.md` | Six film modes and each mode's rule overrides |
| `references/taxonomy.md` | Shots, ~100 transitions, arrival/exit/emphasis states, anchors |
| `references/recipes.md` | 25 step-by-step recipes (intro, feature reveal, before/after, endings…) |
| `references/numbers.md` | Easing, durations, scale, blur and type size, by mode |
| `references/cases/` | 59 shot-by-shot film breakdowns and cross-film comparisons |
| `templates/storyboard.md` | Fill this in before animating |
| `examples/` | A working 20 s film engine, a frame-accurate renderer, a contact-sheet slicer |

Rendering to MP4 needs Node.js with `playwright-core`, a Chromium binary and ffmpeg. The films also play directly in a browser.

## Notes

- The case studies are analytical notes on publicly released launch films, written for study. All brands and films mentioned belong to their owners.
- Contributions are welcome: see `references/analysis-brief.md` for how new films are studied and added.

## License

[MIT](LICENSE) © Mohamed Hassan
