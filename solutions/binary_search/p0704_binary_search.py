"""704. Binary Search
https://leetcode.com/problems/binary-search/

Return the index of a target in a sorted array, or -1 if it is absent.

Approach: Classic binary search that halves the search range each step.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
