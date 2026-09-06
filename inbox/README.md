# inbox

Staging area for raw LeetCode submissions before they are organized.

Drop accepted `.py` files here (named by problem slug, e.g. `two-sum.py` or
`0001-two-sum.py`), then run `python scripts/organize.py --inbox inbox`. The
script classifies each by LeetCode topic tags and moves it into the right
`solutions/<pattern>/` folder.

Raw `.py` files and processed `.done` markers in this folder are gitignored —
only the organized solutions get committed.
