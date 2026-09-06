"""1524. Number of Sub-arrays With Odd Sum
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Count subarrays whose sum is odd, returned modulo 1e9 + 7.

Approach: A subarray sum is odd when its two bounding prefix sums have different
parity, so tally prefixes of each parity and pair opposites as we scan.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        remainder_map = {}
        count = 0
        for i in range(len(prefix)):
            parity = prefix[i] % 2
            if parity == 0 and 1 in remainder_map:
                count += remainder_map[1]
            elif parity == 1 and 0 in remainder_map:
                count += remainder_map[0]
            remainder_map[parity] = remainder_map.get(parity, 0) + 1
        return count % mod
