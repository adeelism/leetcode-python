"""209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Return the length of the shortest contiguous subarray whose sum is at least
target, or 0 if none exists.

Approach: Expand the window adding each number, then shrink from the left while
the running sum still meets target, recording the smallest length.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_window = float("inf")
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                window = right - left + 1
                min_window = min(min_window, window)
                current_sum -= nums[left]
                left += 1
        if min_window == float("inf"):
            return 0
        return min_window
