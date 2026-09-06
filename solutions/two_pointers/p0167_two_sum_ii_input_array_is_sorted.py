"""167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Find the two 1-indexed positions in a sorted array whose values sum to the target.

Approach: Two pointers from both ends; move left in when the sum is too small, right in
when too large, until the pair is found.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return []
