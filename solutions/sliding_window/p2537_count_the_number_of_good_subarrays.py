"""2537. Count the Number of Good Subarrays
https://leetcode.com/problems/count-the-number-of-good-subarrays/

Count the contiguous subarrays that contain at least k pairs of equal elements.

Approach: Slide a window tracking the pair count; once a window has at least k
pairs, every extension to the end is also good, so add (n - right) and shrink.
Time:  O(n)
Space: O(n)
"""


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        left = 0
        n = len(nums)
        count = 0
        freq = {}
        pairs = 0
        for right in range(n):
            num = nums[right]
            pairs += freq.get(nums[right], 0)
            freq[num] = freq.get(num, 0) + 1
            while pairs >= k:
                count += n - right
                left_num = nums[left]
                freq[left_num] -= 1
                pairs -= freq[left_num]
                left += 1
        return count
