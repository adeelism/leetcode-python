"""1893. Check if All the Integers in a Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

Check whether every integer in [left, right] is covered by at least one range.

Approach: Line sweep / difference array. Mark +1 at each range start and -1
just past each range end, take a running prefix sum, and confirm every index in
[left, right] has positive coverage.
Time:  O(n + limit)
Space: O(limit)
"""


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        n = max(end for _, end in ranges)
        limit = max(n, right)
        diff = [0] * (limit + 2)
        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1

        coverage = 0
        for i in range(1, limit + 1):
            coverage += diff[i]
            if left <= i <= right and coverage == 0:
                return False
        return True
