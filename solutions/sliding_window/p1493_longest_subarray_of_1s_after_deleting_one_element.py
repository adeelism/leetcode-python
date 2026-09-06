"""1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Return the longest run of 1s after deleting exactly one element from the array.

Approach: Slide a window allowing at most one zero; the answer is the longest such
window minus one, since one element must always be removed.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        remove_count = 0
        answer = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                remove_count += 1
            while remove_count > 1:
                if nums[left] == 0:
                    remove_count -= 1
                left += 1
            window = right - left + 1
            answer = max(answer, window)
        return answer - 1
