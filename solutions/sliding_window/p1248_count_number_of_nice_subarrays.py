"""1248. Count Number of Nice Subarrays
https://leetcode.com/problems/count-number-of-nice-subarrays/

Count the contiguous subarrays that contain exactly k odd numbers.

Approach: Treat odd numbers as 1 and evens as 0; the problem becomes counting
subarrays summing to k, solved with prefix sums and a frequency map.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            if nums[i] % 2 == 1:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        count = 0
        freq = {}
        for i in range(len(prefix)):
            required = prefix[i] - k
            if required in freq:
                count += freq[required]
            freq[prefix[i]] = freq.get(prefix[i], 0) + 1
        return count
