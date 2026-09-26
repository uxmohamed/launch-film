# launch-film

A [Claude Code](https://claude.com/claude-code) skill for making product launch videos at the level of top studio launch work. It covers concept, storyboard, animation and render.

It was reverse-engineered from a frame-by-frame study of **59 real launch films** (7,495 frames): product launches, brand and identity films, model announcements, hardware spots and founder documentaries. The skill doesn't copy any one film. It encodes the *system* behind them, so you can make new films that feel like the same team made them.

## What it teaches Claude

- **13 universal laws** that held across all 59 films, for example:
  - one spine;
  - one brand "atom" that carries the transitions;
  - a carrier across every cut;
  - chapters coded by the background;
  - show the product's verb;
  - a 0.5-second pulse;
  - one register and one deliberate inversion;
  - end by clearing the stage.
- **Six film modes**, each with its own rule overrides: product/SaaS, creative tool, brand/identity, manifesto/model, hardware, founder documentary.
- **A taxonomy:** ~13 shot types; ~100 transitions; states for how things enter, leave and get emphasis; anchor types; annotation layers; cursor design; ways to show time passing.
- **25 recipes:** introducing the product, revealing a feature, full view → detail, interactions, rapid features, before/after, dashboards, UI ↔ type, endings, and more.
- **Numbers:** easing curves by role, and durations, scale, blur, opacity and type sizes, all given per mode.
- **A production workflow and QC checklist,** plus a storyboard template to fill in before animating.
- **A render pipeline:** a deterministic `render(t)` HTML timeline, frame-accurate capture with headless Chromium, and an ffmpeg encode. A working 20 s example film is included.

## Install

```bash
git clone https://github.com/uxmohamed/launch-film ~/.claude/skills/launch-film
```

Claude Code picks the skill up automatically in your next session. To use it only inside one project, clone it into `<project>/.claude/skills/launch-film` instead.

## Use

Just ask. For example:

- "Make a launch video for https://example.com. Use the site's assets, copy and visual style."
- "Storyboard a 30-second teaser for our new search feature."
- "Critique this launch video against the playbook."
- "Turn these UI screenshots into a cinematic feature reveal."

You can also call it directly with `/launch-film`.

## What's inside

```
SKILL.md                     # the manual: philosophy, laws, modes table, workflow, QC checklist
references/
  modes.md                   # six film modes + rule overrides (read first)
  taxonomy.md                # shots, transitions, arrival/exit/emphasis states, anchors
  recipes.md                 # 25 step-by-step recipes
  numbers.md                 # durations, easing, scale, blur, type, all by mode
  implementation.md          # build + render pipeline, review loop, common bugs
  cases/                     # 59 shot-by-shot film breakdowns + cross-film comparisons
templates/storyboard.md      # fill this in before animating
examples/
  cadie-film.html            # a complete 20 s film built on the engine
  render.js                  # frame capture → MP4 (Playwright + ffmpeg)
  contact_sheet_slicer.py    # slice frame grids into numbered contact sheets
```

## Rendering requirements

To render to MP4 (optional; the HTML films also play in any browser):

- Node.js with `playwright-core` and a Chromium or headless-shell binary;
- ffmpeg;
- Python 3 with `numpy` and `scipy`, if you generate soundtracks.

## Notes

- The case studies are analytical notes written from frame breakdowns of publicly released launch films, for study purposes. All brands, films and products mentioned belong to their owners.
- Timings in the case files were measured from frames sampled at ~2 fps, so treat durations as ±15%. Easing values were calibrated against one film studied at its native 25 fps.
