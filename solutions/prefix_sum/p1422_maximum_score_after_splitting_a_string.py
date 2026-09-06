"""1422. Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Split a binary string in two and maximize the zeros on the left plus the ones on the right.

Approach: Start with all ones on the right, then sweep each split point moving one
character left, updating the zero/one running counts and tracking the best score.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zeroes = 0
        ones = s.count("1")
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeroes += 1
            else:
                ones -= 1
            max_score = max(max_score, zeroes + ones)
        return max_score
