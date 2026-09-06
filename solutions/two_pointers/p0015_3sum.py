"""15. 3Sum
https://leetcode.com/problems/3sum/

Find all unique triplets in the array that sum to zero.

Approach: Sort, fix each number, then two-pointer scan for the remaining pair that
sums to its negation; skip duplicates to keep triplets unique.
Time:  O(n^2)
Space: O(1) extra (excluding output)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n - 2):
            fixed = nums[i]
            if i > 0 and fixed == nums[i - 1]:
                continue
            # All remaining numbers are >= fixed > 0, so no triplet can reach 0.
            if fixed > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[right]
                target = -fixed
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    triplets.append([fixed, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return triplets
