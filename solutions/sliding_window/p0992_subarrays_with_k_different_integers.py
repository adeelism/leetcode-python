"""992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/

Count the contiguous subarrays containing exactly k distinct integers.

Approach: Exactly-k equals (at-most-k) minus (at-most-(k-1)); each at-most helper
slides a window and adds (right - left + 1) valid subarrays per step.
Time:  O(n)
Space: O(k)
"""


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k: int) -> int:
            left = 0
            freq = {}
            count = 0
            distinct = 0
            for right in range(len(nums)):
                num = nums[right]
                if freq.get(num, 0) == 0:
                    distinct += 1
                freq[num] = freq.get(num, 0) + 1
                while distinct > k:
                    left_num = nums[left]
                    freq[left_num] -= 1
                    if freq[left_num] == 0:
                        distinct -= 1
                    left += 1
                count += right - left + 1
            return count

        return atmost(k) - atmost(k - 1)
