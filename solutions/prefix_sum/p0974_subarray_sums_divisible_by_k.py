"""974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Count the non-empty subarrays whose sum is divisible by k.

Approach: Two prefix sums with the same remainder mod k enclose a divisible
subarray; tally how many earlier prefixes share each remainder.
Time:  O(n)
Space: O(k)
"""


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0
        freq = {}
        for i in range(len(prefix)):
            required = prefix[i] % k
            if required in freq:
                count += freq[required]
            freq[required] = freq.get(required, 0) + 1
        return count
