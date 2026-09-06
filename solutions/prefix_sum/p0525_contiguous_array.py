"""525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Find the longest contiguous subarray containing equal numbers of 0s and 1s.

Approach: Treat 0 as -1 so a balanced subarray has prefix-sum difference of zero;
record the first index of each running sum and track the widest matching span.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            if nums[i] == 0:
                prefix[i + 1] = prefix[i] - 1
            else:
                prefix[i + 1] = prefix[i] + 1

        first_seen = {}
        max_len = 0
        for i in range(len(prefix)):
            if prefix[i] in first_seen:
                max_len = max(max_len, i - first_seen[prefix[i]])
            else:
                first_seen[prefix[i]] = i
        return max_len
