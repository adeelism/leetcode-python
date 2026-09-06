"""424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Return the longest substring achievable by replacing at most k characters so all
characters in it become equal.

Approach: Slide a window and track the count of its most frequent character; the
window is valid while (length - max_freq) <= k, shrinking from the left otherwise.
Time:  O(n)
Space: O(alphabet)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0
        max_freq = 0
        letters = {}
        for right in range(len(s)):
            right_letter = s[right]
            letters[right_letter] = letters.get(right_letter, 0) + 1
            max_freq = max(max_freq, letters[right_letter])
            window = right - left + 1
            while window - max_freq > k:
                letters[s[left]] -= 1
                left += 1
                window = right - left + 1
            answer = max(answer, window)
        return answer
