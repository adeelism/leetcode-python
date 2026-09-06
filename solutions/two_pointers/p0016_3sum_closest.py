"""16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Find the triplet whose sum is closest to a given target and return that sum.

Approach: Sort, fix each number, then two-pointer scan tracking the sum with the
smallest absolute distance to target.
Time:  O(n^2)
Space: O(1)
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(target - summ) < abs(target - closest):
                    closest = summ
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    return summ
        return closest
