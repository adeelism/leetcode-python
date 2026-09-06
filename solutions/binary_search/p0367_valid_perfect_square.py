"""367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/

Decide whether a positive integer is the square of some integer.

Approach: Binary search the candidate root in [0, num] and compare its square to num.
Time:  O(log num)
Space: O(1)
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = mid * mid
            if sqrt == num:
                return True
            elif sqrt < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
