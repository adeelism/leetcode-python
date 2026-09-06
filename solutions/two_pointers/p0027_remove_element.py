"""27. Remove Element
https://leetcode.com/problems/remove-element/

Remove all occurrences of a value in-place and return the count of remaining elements.

Approach: Same-direction two pointers; slow is the write position, fast keeps every
element that is not equal to the target value.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
