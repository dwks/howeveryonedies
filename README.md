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

Four pages, with a top navbar between them:

| Page | Holds |
| --- | --- |
| `index.html` | Landing: the four mechanisms as a grid, explanation and scenarios below. |
| `mechanisms.html` | Part M |
| `explanation.html` | Part E |
| `scenarios.html` | Part S |

## Files

| File | Purpose |
| --- | --- |
| `src/*.html` | The page bodies. Edit these. |
| `styles.css` | All styling, light and dark themes. |
| `build.py` | Assembles the site and the artifact bundle. |
| `*.html`, `artifact/` | Generated. Do not edit by hand. |
| `ideas.txt` | Working outline. |

```sh
./build.py
```

Partials cross-link with `{{href <view>}}` or `{{href <view> <anchor>}}`, which
the build resolves per output. The site gets four real pages that work without
JavaScript; a published Claude Artifact is a single page, so `artifact/page.html`
bundles all four views behind a hash router from the same sources.
