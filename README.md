# How Everyone Dies

A draft site registering the *mechanisms* by which advanced AI could kill
everyone — a companion to *If Anyone Builds It, Everyone Dies*, which argues
the **if**. This asks the **how**.

Published draft: <https://claude.ai/artifact/3ehNhVFAw8UoXfx2TtegL4>

Twelve entries in three parts:

- **M** — four independent mechanisms (gradual disempowerment, the impossible
  task, the move you never see, boil the oceans)
- **E** — four ordered steps to explaining the risk (goals, harm, intervention,
  exponentials)
- **S** — four existing scenarios summarised (AI 2027, AI 2040: Plan A,
  Yudkowsky's nanotech lower bound, ten framings of gradual disempowerment)

## Structure

The served site is `dist/`. Four pages, with a top navbar between them:

| Page | Holds |
| --- | --- |
| `dist/index.html` | Landing: the intro, the four mechanisms as a grid, explanation and scenarios below. |
| `dist/mechanisms.html` | Part M |
| `dist/explanation.html` | Part E |
| `dist/scenarios.html` | Part S |

## Files

| Path | Purpose |
| --- | --- |
| `src/*.html` | The page bodies. Edit these. |
| `src/styles.css` | All styling. Maroon palette, light and dark themes. |
| `build.py` | Assembles `dist/`. |
| `dist/` | Generated. Do not edit by hand. |
| `ideas.txt`, `text.txt` | Working notes and copy. |

```sh
./build.py
```

Partials cross-link with `{{href <view>}}` or `{{href <view> <anchor>}}`, which
the build resolves per output. The site gets four real pages that work without
JavaScript; `dist/artifact.html` bundles all four views behind a hash router for
publishing as a Claude Artifact, which is only ever a single page. It is built
from the same sources and is not part of the served site.
