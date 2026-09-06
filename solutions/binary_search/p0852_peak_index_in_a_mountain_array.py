"""852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Find the index of the peak element in a strictly increasing-then-decreasing array.

Approach: Binary search comparing each mid with its neighbor; move right when still
ascending, otherwise keep mid as a peak candidate until the bounds converge.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
