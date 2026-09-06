"""2009. Minimum Number of Operations to Make Array Continuous
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

Return the fewest replacements needed so the array holds n distinct values that
form a run of consecutive integers.

Approach: Sort the unique values; slide a window that fits inside a range of size
n and keep the most values retainable, replacing the rest.
Time:  O(n log n)
Space: O(n)
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))
        left = 0
        max_keep_elements = 0
        for right in range(len(unique_nums)):
            while unique_nums[right] - unique_nums[left] > n - 1:
                left += 1
            window = right - left + 1
            max_keep_elements = max(max_keep_elements, window)
        return n - max_keep_elements
