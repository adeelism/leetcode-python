"""1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Return the longest run of 1s obtainable by flipping at most k zeros.

Approach: Slide a window counting zeros inside it; when the zero count exceeds k,
shrink from the left until at most k zeros remain.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            window = right - left + 1
            ans = max(ans, window)
        return ans
