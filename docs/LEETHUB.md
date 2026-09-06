# Auto-committing future submissions

New accepted submissions can land in this repo automatically, in the right
pattern folder, using a browser extension.

## Recommended: LeetHub v3 (or an equivalent)

[LeetHub v3](https://github.com/arreic/LeetHub-3.0) is a maintained Chrome
extension that commits each accepted LeetCode submission to a GitHub repository.
(The original `LeetHub` is unmaintained; use a current fork.)

### Setup

1. Install the extension from the Chrome Web Store.
2. Authenticate it with GitHub and point it at a repository — either this one
   (`leetcode-python`) or a dedicated raw repo it fully controls.
3. Solve a problem and submit. On **Accepted**, the extension pushes the
   solution and a small notes file.

### How it fits this repo's layout

LeetHub-style extensions organize by **problem**, not by **pattern**, so their
output does not match `solutions/<pattern>/` directly. Two workable options:

- **Option A (recommended): a separate inbox repo.** Let the extension push to a
  repo it owns (e.g. `leetcode-raw`). Periodically move new solutions here,
  dropping each into its pattern folder and adding the docstring + a test. This
  keeps this repo curated while capturing everything automatically.
- **Option B: push here, curate in place.** Point the extension at this repo; it
  creates per-problem folders at the root. On a cadence, relocate them under the
  correct `solutions/<pattern>/` folder and add a test.

Either way, the curation step is: **classify → add complexity docstring → add a
test → move into the pattern folder.**

## Note on problem statements

LeetCode problem text is LeetCode's copyrighted content, so it is **not**
committed here. Each solution file references the problem by title and URL and
paraphrases the task in one line — the code is yours; the prompt stays on
LeetCode.
