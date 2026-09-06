"""724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

Find the leftmost index where the sum to its left equals the sum to its right.

Approach: With a prefix-sum array, the left sum at index i is prefix[i] and the
right sum is prefix[n] - prefix[i + 1]; return the first index where they match.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        for i in range(n):
            if prefix[i] == prefix[n] - prefix[i + 1]:
                return i
        return -1
