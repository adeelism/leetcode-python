"""303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Answer repeated queries for the sum of elements in an inclusive index range.

Approach: Precompute a prefix-sum array once so each query is a constant-time
subtraction prefix[right + 1] - prefix[left].
Time:  O(n) build, O(1) per query
Space: O(n)
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
