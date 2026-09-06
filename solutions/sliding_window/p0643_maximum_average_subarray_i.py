"""643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Return the maximum average over all contiguous subarrays of length k.

Approach: Build the first window's sum, then slide it one element at a time,
adding the entering value and removing the leaving one, tracking the best average.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        max_avg = curr_sum / k
        for i in range(k, n):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            avg = curr_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
