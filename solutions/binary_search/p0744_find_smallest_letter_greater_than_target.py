"""744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Return the smallest letter strictly greater than target, wrapping to the first letter.

Approach: Binary search for the first letter greater than target, tracking the best
candidate; the initial answer of letters[0] handles the wrap-around case.
Time:  O(log n)
Space: O(1)
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        ans = letters[0]
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                ans = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        return ans
