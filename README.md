# How Everyone Dies

A draft site registering the *mechanisms* by which advanced AI could kill
everyone — a companion to *If Anyone Builds It, Everyone Dies*, which argues
the **if**. This asks the **how**.

Twelve entries in three parts:

- **M** — four independent mechanisms (gradual disempowerment, the impossible
  task, the move you never see, boil the oceans)
- **E** — four ordered steps to explaining the risk (goals, harm, intervention,
  exponentials)
- **S** — four existing scenarios summarised (AI 2027, AI 2040: Plan A,
  Yudkowsky's nanotech lower bound, ten framings of gradual disempowerment)

## Files

| File | Purpose |
| --- | --- |
| `content.html` | The page. Edit this. A `<!-- @body -->` sentinel divides head from body. |
| `styles.css` | All styling, light and dark themes. |
| `build.sh` | Wraps `content.html` in a standalone document → `index.html`. |
| `index.html` | Generated. Do not edit by hand. |
| `ideas.txt` | Working outline. |

```sh
./build.sh
```

`content.html` doubles as the Claude Artifact source, which supplies its own
`<html>`/`<head>` skeleton — hence the split.
