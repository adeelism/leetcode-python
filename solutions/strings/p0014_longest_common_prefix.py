"""14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Find the longest string that is a prefix of every string in the list.

Approach: Compare characters of the first string against the others column by
column; stop at the first mismatch or when a string runs out.
Time:  O(n * m) where n is the number of strings and m the shortest length
Space: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        base = strs[0]
        for i in range(len(base)):
            char = base[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return base[:i]
        return base
