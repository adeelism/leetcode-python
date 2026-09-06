"""35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Return the index of a target in a sorted array, or where it would be inserted.

Approach: Standard binary search; on failure the left pointer lands on the correct
insertion point.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
