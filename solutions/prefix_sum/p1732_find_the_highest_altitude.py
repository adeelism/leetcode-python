"""1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/

Starting at altitude 0, find the highest altitude reached given the gains between points.

Approach: Keep a running altitude (a prefix sum of the gains) and track its maximum.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = 0
        highest = 0
        for g in gain:
            current += g
            highest = max(highest, current)
        return highest
