"""1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Count the length-k subarrays whose average is at least threshold.

Approach: Slide a fixed window of size k comparing its sum against k * threshold,
avoiding division.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        current_sum = 0
        result = 0
        for i in range(k):
            current_sum += arr[i]
        if current_sum >= target_sum:
            result += 1
        for i in range(k, len(arr)):
            current_sum += arr[i]
            current_sum -= arr[i - k]
            if current_sum >= target_sum:
                result += 1
        return result
