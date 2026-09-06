"""125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Check whether a string reads the same forwards and backwards, ignoring case and
non-alphanumeric characters.

Approach: Filter to lowercase alphanumerics, then two pointers from both ends compare
characters moving inward.
Time:  O(n)
Space: O(n) for the filtered string
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = "".join(char for char in s if char.isalnum()).lower()
        if lower_s == "":
            return True
        left = 0
        right = len(lower_s) - 1
        while left < right:
            if lower_s[left] != lower_s[right]:
                return False
            left += 1
            right -= 1
        return True
