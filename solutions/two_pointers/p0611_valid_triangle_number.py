"""611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/

Count triplets from the array that can form the sides of a valid triangle.

Approach: Sort, fix the largest side, then two pointers over the smaller elements; when
the two smaller sides exceed the fixed side, all pairs between them also qualify.
Time:  O(n^2)
Space: O(1)
"""


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                two_sides = nums[left] + nums[right]
                if two_sides > nums[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result
