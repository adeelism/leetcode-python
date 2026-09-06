"""Organize raw LeetCode submissions into the right pattern folder.

New accepted submissions (e.g. pushed by a LeetHub-style extension into an
`inbox/` folder) are classified by LeetCode's own topic tags, renamed to the
canonical frontend problem number, wrapped with the standard docstring header,
and moved under `solutions/<pattern>/`, with a test stub under `tests/<pattern>/`.
Per-pattern README tables are regenerated afterward.

Usage:
    python scripts/organize.py --inbox inbox         # organize an inbox folder
    python scripts/organize.py --classify two-sum    # just print the pattern
    python scripts/organize.py --inbox inbox --dry-run
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# LeetCode topic-tag slug -> local pattern folder, in priority order (the first
# matching tag on a problem wins). Unmapped problems fall back to arrays_hashing.
PRIORITY: list[tuple[str, str]] = [
    ("two-pointers", "two_pointers"),
    ("sliding-window", "sliding_window"),
    ("binary-search", "binary_search"),
    ("prefix-sum", "prefix_sum"),
    ("dynamic-programming", "dynamic_programming"),
    ("backtracking", "backtracking"),
    ("depth-first-search", "graphs"),
    ("breadth-first-search", "graphs"),
    ("graph", "graphs"),
    ("union-find", "graphs"),
    ("binary-tree", "trees"),
    ("tree", "trees"),
    ("trie", "tries"),
    ("heap-priority-queue", "heap"),
    ("stack", "stack"),
    ("monotonic-stack", "stack"),
    ("queue", "stack"),
    ("linked-list", "linked_list"),
    ("greedy", "greedy"),
    ("bit-manipulation", "bit_manipulation"),
    ("string", "strings"),
    ("math", "math"),
    ("hash-table", "arrays_hashing"),
    ("array", "arrays_hashing"),
]
FALLBACK = "arrays_hashing"

DOC_TEMPLATE = '''"""{number}. {title}
https://leetcode.com/problems/{slug}/

TODO: one-line paraphrase of the task.

Approach: TODO.
Time:  O(?)
Space: O(?)
"""
'''

TEST_TEMPLATE = """from solutions.{pattern}.{module} import Solution  # noqa: F401


def test_importable():
    # TODO: replace with real example cases (assert Solution().method(...) == ...).
    assert Solution is not None
"""


def query(slug: str) -> dict:
    body = json.dumps(
        {
            "query": (
                "query q($slug:String!){question(titleSlug:$slug)"
                "{questionFrontendId title topicTags{slug}}}"
            ),
            "variables": {"slug": slug},
        }
    ).encode()
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)["data"]["question"]


def pattern_for(tags: list[str]) -> str:
    tagset = set(tags)
    for tag, folder in PRIORITY:
        if tag in tagset:
            return folder
    return FALLBACK


def slug_from(name: str) -> str:
    base = re.sub(r"\.py$", "", os.path.basename(name))
    return re.sub(r"^\d+[-_]", "", base).replace("_", "-")


def ensure_package(*dirs: str) -> None:
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        init = os.path.join(directory, "__init__.py")
        if directory.startswith(os.path.join(REPO, "solutions")) and not os.path.exists(init):
            open(init, "w", encoding="utf-8").close()


def organize_one(py_path: str, dry_run: bool) -> tuple[str, str] | None:
    slug = slug_from(py_path)
    question = query(slug)
    if not question:
        print(f"  ! could not resolve '{slug}' on LeetCode; skipping")
        return None
    number = int(question["questionFrontendId"])
    title = question["title"]
    pattern = pattern_for([t["slug"] for t in question["topicTags"]])
    module = f"p{number:04d}_{slug.replace('-', '_')}"
    print(f"  {slug} -> {pattern}/{module}")
    if dry_run:
        return number, pattern

    sol_dir = os.path.join(REPO, "solutions", pattern)
    test_dir = os.path.join(REPO, "tests", pattern)
    ensure_package(sol_dir, test_dir)

    code = open(py_path, encoding="utf-8").read().strip()
    header = DOC_TEMPLATE.format(number=number, title=title, slug=slug)
    sol_path = os.path.join(sol_dir, f"{module}.py")
    open(sol_path, "w", encoding="utf-8").write(header + "\n" + code + "\n")

    test_path = os.path.join(test_dir, f"test_{module}.py")
    if not os.path.exists(test_path):
        test_body = TEST_TEMPLATE.format(pattern=pattern, module=module)
        open(test_path, "w", encoding="utf-8").write(test_body)
    return number, pattern


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inbox", default="inbox", help="folder of raw .py submissions")
    parser.add_argument("--classify", help="print the pattern for a single problem slug and exit")
    parser.add_argument("--dry-run", action="store_true", help="classify without writing files")
    args = parser.parse_args()

    if args.classify:
        question = query(args.classify)
        print(pattern_for([t["slug"] for t in question["topicTags"]]) if question else "unknown")
        return

    inbox = os.path.join(REPO, args.inbox) if not os.path.isabs(args.inbox) else args.inbox
    files = sorted(glob.glob(os.path.join(inbox, "**", "*.py"), recursive=True))
    if not files:
        print(f"No .py files found under {inbox}")
        return

    print(f"Organizing {len(files)} submission(s) from {inbox}:")
    organized = 0
    for py_path in files:
        if organize_one(py_path, args.dry_run):
            organized += 1
            if not args.dry_run:
                shutil.move(py_path, py_path + ".done")

    print(f"\nOrganized {organized} submission(s).")
    if not args.dry_run and organized:
        print("Next: fill in each new file's Approach/complexity and real test cases,")
        print("then run: python scripts/gen_readmes.py  (regenerates the pattern tables)")


if __name__ == "__main__":
    main()
