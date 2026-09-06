"""1. Two Sum
https://leetcode.com/problems/two-sum/

Return the indices of the two numbers that add up to the target.

Approach: Keep a hash map of previously seen values to their indices; for each
number check whether its complement has already been seen.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
        return []
