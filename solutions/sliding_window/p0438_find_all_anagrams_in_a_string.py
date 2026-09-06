"""438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Return the start indices of every substring of s that is an anagram of p.

Approach: Keep a fixed-size window of length len(p) and compare its character
frequency map against p's, sliding one step at a time.
Time:  O(|s|)
Space: O(alphabet)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        mapping = {}
        p_map = {}
        result = []
        if len(p) > len(s):
            return result
        for i in range(len(p)):
            mapping[s[i]] = mapping.get(s[i], 0) + 1
            p_map[p[i]] = p_map.get(p[i], 0) + 1
        if p_map == mapping:
            result.append(0)

        for right in range(len(p), len(s)):
            left = right - len(p)
            mapping[s[right]] = mapping.get(s[right], 0) + 1
            mapping[s[left]] -= 1
            if mapping[s[left]] == 0:
                del mapping[s[left]]
            if mapping == p_map:
                result.append(left + 1)
        return result
