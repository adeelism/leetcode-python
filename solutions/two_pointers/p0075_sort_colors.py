"""75. Sort Colors
https://leetcode.com/problems/sort-colors/

Sort an array of 0s, 1s, and 2s in-place in a single pass.

Approach: Dutch national flag with three pointers (low, mid, high) partitioning the
array into confirmed 0s, 1s, unknown, and 2s regions.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """Modify nums in-place; return nothing."""
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
