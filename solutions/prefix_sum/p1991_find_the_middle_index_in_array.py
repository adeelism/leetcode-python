"""1991. Find the Middle Index in Array
https://leetcode.com/problems/find-the-middle-index-in-array/

Find the leftmost index where the sum of elements to its left equals the sum to its right.

Approach: Track a running left sum and derive the right sum as total - left - current,
returning the first index where the two sides balance.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
