"""1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Return the running (cumulative) sum of the array at each index.

Approach: Keep a rolling total and append it after adding each element.
Time:  O(n)
Space: O(1) extra (output array excluded)
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0
        for num in nums:
            total += num
            result.append(total)
        return result
