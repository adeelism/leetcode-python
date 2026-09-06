"""1695. Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/

Return the maximum sum of a contiguous subarray whose elements are all distinct.

Approach: Slide a window keeping a set of its values and a running sum; when a
duplicate arrives, shrink from the left until the value is unique again.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        max_score = 0
        left = 0
        seen = set()
        current_sum = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            current_sum += nums[right]
            max_score = max(max_score, current_sum)
        return max_score
