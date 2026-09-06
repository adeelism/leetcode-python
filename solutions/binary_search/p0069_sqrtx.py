"""69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Compute the integer square root of x (floor of the true square root).

Approach: Binary search the answer in [0, x], comparing mid against x // mid to avoid
overflow, and keep the largest mid whose square does not exceed x.
Time:  O(log x)
Space: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid <= x // mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
