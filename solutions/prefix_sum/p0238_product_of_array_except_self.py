"""238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Return an array where each position holds the product of every element except the one at that index.

Approach: Accumulate running prefix products left-to-right into the answer, then
multiply in the suffix products right-to-left using a single scalar.
Time:  O(n)
Space: O(1) extra (output array excluded)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
