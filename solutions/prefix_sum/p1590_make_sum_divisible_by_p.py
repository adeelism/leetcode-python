"""1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/

Remove the shortest subarray so the remaining elements sum to a multiple of p.

Approach: Let the total's remainder be r; we need a subarray whose remainder is r.
Scan prefixes, look up the most recent prefix whose remainder makes the gap divisible,
and track the shortest such subarray.
Time:  O(n)
Space: O(min(n, p))
"""


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total_remainder = prefix[n] % p
        if total_remainder == 0:
            return 0

        min_length = n
        freq = {}
        for i in range(len(prefix)):
            current_remainder = prefix[i] % p
            needed = (current_remainder - total_remainder) % p
            if needed in freq:
                min_length = min(min_length, i - freq[needed])
            freq[current_remainder] = i

        if min_length == n:
            return -1
        return min_length
