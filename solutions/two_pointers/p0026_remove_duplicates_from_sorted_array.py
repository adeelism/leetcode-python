"""26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Remove duplicates in-place from a sorted array and return the count of unique values.

Approach: Same-direction two pointers; slow marks the last kept unique value, fast
scans and overwrites the next slot when a new value appears.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
