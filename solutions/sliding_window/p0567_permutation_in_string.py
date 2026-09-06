"""567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Return True if s2 contains any permutation of s1 as a contiguous substring.

Approach: Slide a fixed window of length len(s1) over s2 and check whether the
window's character-frequency map matches s1's.
Time:  O(|s2|)
Space: O(alphabet)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
        s1_freq = {}
        window_freq = {}
        for i in range(k):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1
        if s1_freq == window_freq:
            return True

        for i in range(k, len(s2)):
            left = i - k
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1
            window_freq[s2[left]] -= 1
            if window_freq[s2[left]] == 0:
                del window_freq[s2[left]]
            if window_freq == s1_freq:
                return True
        return False
