# Auto-organizing future submissions

New accepted submissions can be filed into the correct pattern folder
automatically, using a browser extension to capture them plus the
`scripts/organize.py` helper to classify and place them.

## 1. Capture: a LeetHub-style extension

[LeetHub v3](https://github.com/arreic/LeetHub-3.0) (a maintained fork; the
original `LeetHub` is unmaintained) commits each accepted submission to a GitHub
repo. Install it, authenticate with GitHub, and point it at a repo it controls
(a dedicated `leetcode-raw` inbox repo is cleanest).

## 2. Classify + place: `scripts/organize.py`

Drop the raw `.py` submissions into this repo's `inbox/` folder (copy them from
the extension's repo, or export with `leetcode-export`), then run:

```bash
python scripts/organize.py --inbox inbox
```

For each submission the script:

1. Reads the problem **slug** from the filename.
2. Queries LeetCode's public GraphQL API for the **canonical frontend number**,
   title, and **topic tags** — so numbering is always correct (the exporters use
   LeetCode's internal id, which differs for ~half of problems).
3. Maps the topic tags to a pattern folder (`two-pointers` → `two_pointers`,
   `sliding-window` → `sliding_window`, `dynamic-programming` →
   `dynamic_programming`, …; unmapped problems fall back to `arrays_hashing`).
4. Writes `solutions/<pattern>/pNNNN_<slug>.py` with the standard docstring
   header (title, link, and `TODO` for the paraphrase/approach/complexity), plus
   a test stub under `tests/<pattern>/`.

Check where a problem would land without writing anything:

```bash
python scripts/organize.py --classify longest-substring-without-repeating-characters
# -> sliding_window
python scripts/organize.py --inbox inbox --dry-run
```

## 3. Curate + commit (the human step)

The script gets each solution into the right folder with a correct name; you
then:

- fill in the one-line paraphrase, **Approach**, and **Time/Space**;
- replace the test stub with real example cases;
- run `python scripts/gen_readmes.py` to refresh the pattern tables;
- `ruff check --fix . && ruff format . && pytest`, then commit.

This keeps the repo curated and its CI green, while removing the tedious part —
figuring out the canonical number and the right pattern folder.

> Fully automatic commit-from-CI is intentionally not wired up: raw submissions
> usually need a small cleanup (a paraphrase, real test cases, an unused-import
> fix) before they'd pass this repo's lint/format/test gate.

## Note on problem statements

LeetCode problem text is LeetCode's copyright and is **not** committed here. Each
file links the problem and paraphrases it in one line; only your solution code
lives in the repo.
