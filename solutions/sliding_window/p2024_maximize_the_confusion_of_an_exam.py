"""2024. Maximize the Confusion of an Exam
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

Return the longest run of equal answers achievable by flipping at most k entries
between 'T' and 'F'.

Approach: Slide a window tracking counts of 'T' and 'F'; it stays valid while
(length - max(count)) <= k, otherwise shrink from the left.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        max_len = 0
        count = {"T": 0, "F": 0}
        n = len(answerKey)
        for right in range(n):
            count[answerKey[right]] = count.get(answerKey[right], 0) + 1
            while (right - left + 1) - max(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left += 1
            curr_window = right - left + 1
            max_len = max(max_len, curr_window)
        return max_len
