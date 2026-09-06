"""374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/

Find a picked number in 1..n using a guess oracle that says higher, lower, or correct.

Approach: Binary search over [1, n], moving the bounds based on the oracle's feedback.
Time:  O(log n)
Space: O(1)
"""

# On LeetCode ``guess`` is provided by the judge. Here we expose a testable seam:
# tests set the module global ``_PICK`` to the picked number.
_PICK = 1


def guess(num: int) -> int:
    if num > _PICK:
        return -1
    if num < _PICK:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid
        return -1
