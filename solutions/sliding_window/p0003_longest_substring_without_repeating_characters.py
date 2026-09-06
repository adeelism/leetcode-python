"""3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Return the length of the longest substring of s that contains no repeated character.

Approach: Grow a sliding window; keep the window's characters in a set and shrink
from the left whenever the incoming character is already present.
Time:  O(n)
Space: O(min(n, alphabet))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()
        for right in range(len(s)):
            # shrink until the incoming character is unique in the window
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            window = right - left + 1
            longest = max(longest, window)
            seen.add(s[right])
        return longest
