"""2461. Maximum Sum of Distinct Subarrays With Length K
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

Return the maximum sum of a length-k subarray whose elements are all distinct,
or 0 if none exists.

Approach: Slide a fixed window of size k tracking a running sum and a frequency
map; a window qualifies when the map holds exactly k keys.
Time:  O(n)
Space: O(k)
"""


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        freq = {}
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        if len(freq) == k:
            max_sum = curr_sum
        for i in range(k, len(nums)):
            left = i - k
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            curr_sum -= nums[left]
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            if len(freq) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
