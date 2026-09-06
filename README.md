# leetcode-python

[![CI](https://github.com/adeelism/leetcode-python/actions/workflows/ci.yml/badge.svg)](https://github.com/adeelism/leetcode-python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](./LICENSE)

Accepted LeetCode solutions in Python, organized **by pattern** rather than by
number. Each solution states its approach and time/space complexity, and a
`pytest` suite runs the worked examples so the whole set stays green.

Profile: [leetcode.com/u/adeelism](https://leetcode.com/u/adeelism)

## Layout

```text
solutions/
  <pattern>/
    pNNNN_problem_slug.py     # one problem per file
tests/
  <pattern>/
    test_pNNNN_problem_slug.py # runs the example cases
```

Each solution file follows the same shape:

```python
"""<Number>. <Title>
https://leetcode.com/problems/<slug>/

<one-line paraphrase of the task>

Approach: <short description>
Time:  O(...)
Space: O(...)
"""


class Solution:
    def method(self, ...): ...
```

## Patterns

Each pattern folder has its own table linking every problem.

| Pattern | Solutions |
| --- | --- |
| [Arrays & Hashing](./solutions/arrays_hashing/) | 3 |
| [Two Pointers](./solutions/two_pointers/) | 14 |
| [Sliding Window](./solutions/sliding_window/) | 21 |
| [Binary Search](./solutions/binary_search/) | 9 |
| [Prefix Sum](./solutions/prefix_sum/) | 20 |
| [Strings](./solutions/strings/) | 3 |
| [Math](./solutions/math/) | 1 |
| **Total** | **71** |

## Running the tests

```bash
python -m pip install -r requirements-dev.txt
pytest            # run the example suite
ruff check .      # lint
ruff format .     # format
```

CI runs `ruff check`, `ruff format --check`, and `pytest` on every push and PR.

## Future submissions

New accepted submissions can be auto-committed with a browser extension and then
curated into the right pattern folder — see [docs/LEETHUB.md](./docs/LEETHUB.md).

## Note on problem statements

LeetCode problem text is LeetCode's copyrighted content and is **not** committed
here. Each file links the problem and paraphrases it in one line; the solution
code is mine.

## License

Solution code is [MIT](./LICENSE). Problem statements belong to LeetCode.
