"""560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Count how many contiguous subarrays sum exactly to k.

Approach: For each prefix sum, the number of earlier prefixes equal to
prefix - k gives the subarrays ending here; keep a running frequency map.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        freq = {}
        for i in range(len(prefix)):
            required = prefix[i] - k
            if required in freq:
                count += freq[required]
            freq[prefix[i]] = freq.get(prefix[i], 0) + 1
        return count
