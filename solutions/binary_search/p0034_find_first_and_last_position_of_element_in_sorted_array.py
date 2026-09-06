"""34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Find the starting and ending index of a target value in a sorted array, or [-1, -1].

Approach: Run the same boundary binary search twice, biasing left on a match to find
the first occurrence and biasing right to find the last occurrence.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    ans = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return [find(True), find(False)]
