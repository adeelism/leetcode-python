"""13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Convert a Roman numeral string into its integer value.

Approach: Scan left to right; if a symbol is smaller than the one after it,
subtract its value (subtractive notation), otherwise add it.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        for i in range(len(s)):
            current_num = mapping[s[i]]
            if i + 1 < len(s) and current_num < mapping[s[i + 1]]:
                num -= current_num
            else:
                num += current_num
        return num
