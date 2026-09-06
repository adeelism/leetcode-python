"""76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Return the shortest substring of s that contains every character of t (with
multiplicity), or "" if no such window exists.

Approach: Expand the right edge until the window covers all needed characters,
then shrink from the left while it stays valid, tracking the smallest window.
Time:  O(|s| + |t|)
Space: O(|s| + |t|)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        n = len(s)
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        required_characters = len(t_freq)

        left = 0
        current_window = {}
        formed = 0
        min_len = float("inf")
        min_start = 0
        for right in range(n):
            char = s[right]
            current_window[char] = current_window.get(char, 0) + 1
            if char in t_freq and current_window[char] == t_freq[char]:
                formed += 1
            while formed == required_characters:
                window = right - left + 1
                if window < min_len:
                    min_len = window
                    min_start = left
                left_char = s[left]
                current_window[left_char] -= 1
                if left_char in t_freq and current_window[left_char] < t_freq[left_char]:
                    formed -= 1
                left += 1
        if min_len == float("inf"):
            return ""
        return s[min_start : min_start + min_len]
