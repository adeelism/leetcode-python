"""713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/

Count the contiguous subarrays whose element product is strictly less than k.

Approach: Maintain a window with product < k; when the incoming number pushes the
product too high, shrink from the left, then add (right - left + 1) new subarrays.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
