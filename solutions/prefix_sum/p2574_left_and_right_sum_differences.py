"""2574. Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/

For each index return the absolute difference between its left-side and right-side sums.

Approach: Build prefix (left) and suffix (right) sum arrays, then take the absolute
difference at each index.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        answer = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i])
        return answer
