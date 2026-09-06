"""1266. Minimum Time Visiting All Points
https://leetcode.com/problems/minimum-time-visiting-all-points/

Find the minimum seconds to visit all points in order using 8-directional moves.

Approach: Between two consecutive points the cost is the Chebyshev distance,
max(|dx|, |dy|), because diagonal moves cover one x and one y step at once.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1):
            xdiff = points[i][0] - points[i + 1][0]
            ydiff = points[i][1] - points[i + 1][1]
            steps += max(abs(xdiff), abs(ydiff))
        return steps
