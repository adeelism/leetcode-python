"""283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Move all zeros to the end in-place while preserving the order of non-zero elements.

Approach: Same-direction two pointers; slow marks the next slot for a non-zero value,
swap each non-zero forward only when it is out of place.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """Modify nums in-place; return nothing."""
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if slow != fast:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
