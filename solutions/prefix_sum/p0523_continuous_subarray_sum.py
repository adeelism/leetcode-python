"""523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/

Decide whether some subarray of length >= 2 has a sum that is a multiple of k.

Approach: Two prefix sums with the same remainder mod k bound a subarray whose
sum is divisible by k; remember the first index of each remainder and check the gap.
Time:  O(n)
Space: O(min(n, k))
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        seen = {}
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(len(prefix)):
            remainder = prefix[i] % k
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        return False
