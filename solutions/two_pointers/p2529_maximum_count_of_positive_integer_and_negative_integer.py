"""2529. Maximum Count of Positive Integer and Negative Integer
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

Given a sorted array, return the larger of the count of positive and negative values.

Approach: Binary search for the first index >= 0 (negatives before it) and the first
index >= 1 (positives from it to the end); return the larger count.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        def get_integer_count(target: int) -> int:
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        negative_count = get_integer_count(0)
        positive_count = len(nums) - get_integer_count(1)
        return max(negative_count, positive_count)
