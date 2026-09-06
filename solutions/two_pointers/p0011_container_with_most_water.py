"""11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given bar heights, pick two lines that together with the x-axis hold the most water.

Approach: Two pointers from both ends; area is width * min(height); move the shorter
side inward each step since it limits the area.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            max_water = max(max_water, width * min_height)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_water
