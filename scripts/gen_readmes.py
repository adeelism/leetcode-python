"""Regenerate the per-pattern README tables and print the main summary table."""

import glob
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRETTY = {
    "arrays_hashing": "Arrays & Hashing",
    "two_pointers": "Two Pointers",
    "sliding_window": "Sliding Window",
    "binary_search": "Binary Search",
    "prefix_sum": "Prefix Sum",
    "stack": "Stack",
    "linked_list": "Linked List",
    "trees": "Trees",
    "tries": "Tries",
    "heap": "Heap",
    "backtracking": "Backtracking",
    "graphs": "Graphs",
    "dynamic_programming": "Dynamic Programming",
    "greedy": "Greedy",
    "bit_manipulation": "Bit Manipulation",
    "strings": "Strings",
    "math": "Math",
}


def pretty(name: str) -> str:
    return PRETTY.get(name, name.replace("_", " ").title())


def main() -> None:
    patterns: dict[str, list] = {}
    for path in glob.glob(os.path.join(REPO, "solutions", "*", "p*.py")):
        pattern = os.path.basename(os.path.dirname(path))
        lines = open(path, encoding="utf-8").read().splitlines()
        match = re.match(r'"""(\d+)\.\s*(.+)', lines[0])
        if not match:
            continue
        num, title = int(match.group(1)), match.group(2).strip()
        url = lines[1].strip()
        patterns.setdefault(pattern, []).append((num, title, url, os.path.basename(path)))

    for pattern, items in patterns.items():
        items.sort()
        rows = ["| # | Problem | Solution |", "| --- | --- | --- |"]
        for num, title, url, fname in items:
            rows.append(f"| {num} | [{title}]({url}) | [`{fname}`](./{fname}) |")
        body = f"# {pretty(pattern)}\n\n{len(items)} solutions.\n\n" + "\n".join(rows) + "\n"
        readme = os.path.join(REPO, "solutions", pattern, "README.md")
        open(readme, "w", encoding="utf-8").write(body)

    main_rows = ["| Pattern | Solutions |", "| --- | --- |"]
    total = 0
    for pattern in sorted(patterns, key=lambda p: -len(patterns[p])):
        count = len(patterns[pattern])
        total += count
        main_rows.append(f"| [{pretty(pattern)}](./solutions/{pattern}/) | {count} |")
    main_rows.append(f"| **Total** | **{total}** |")
    print("\n".join(main_rows))


if __name__ == "__main__":
    main()
