"""905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Reorder the array so every even number comes before every odd number.

Approach: Same-direction two pointers; slow marks the next slot for an even value and
each even element found by fast is swapped forward.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums
