"""242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Decide whether one string is an anagram of the other.

Approach: If lengths differ they cannot match; otherwise build character
frequency maps for both strings and compare them.
Time:  O(n)
Space: O(1) since the alphabet is bounded
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
        return s_freq == t_freq
