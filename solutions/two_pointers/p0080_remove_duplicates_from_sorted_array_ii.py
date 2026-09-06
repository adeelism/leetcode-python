"""80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Remove duplicates in-place so each value appears at most twice; return the new length.

Approach: Same-direction two pointers; keep nums[fast] only if it differs from the
value two write-positions back, guaranteeing at most two copies.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = 2
        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
