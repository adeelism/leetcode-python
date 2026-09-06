"""930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/

Count the contiguous subarrays of a 0/1 array whose sum equals goal.

Approach: Build prefix sums and, while scanning, count earlier prefixes equal to
(current prefix - goal) using a frequency map.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        freq = {}
        count = 0
        for i in range(len(prefix)):
            required = prefix[i] - goal
            if required in freq:
                count += freq[required]
            freq[prefix[i]] = freq.get(prefix[i], 0) + 1
        return count
