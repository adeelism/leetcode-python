"""278. First Bad Version
https://leetcode.com/problems/first-bad-version/

Find the first bad version given a monotonic is-bad predicate over versions 1..n.

Approach: Boundary binary search; shrink [1, n] until the left and right pointers
meet on the first version for which the predicate is true.
Time:  O(log n)
Space: O(1)
"""

# On LeetCode ``isBadVersion`` is provided by the judge. Here we expose a testable
# seam: tests set the module global ``_BAD`` to the first bad version.
_BAD = 1


def is_bad_version(version: int) -> bool:
    return version >= _BAD


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if is_bad_version(mid):
                right = mid
            else:
                left = mid + 1
        return left
