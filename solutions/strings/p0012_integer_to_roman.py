"""12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Convert an integer into its Roman numeral representation.

Approach: Greedily subtract the largest value/symbol pairs (including the
subtractive forms like CM and IV) from the number, appending symbols as we go.
Time:  O(1)
Space: O(1)
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        result = []
        for value, symbol in mapping:
            count = num // value
            result.append(symbol * count)
            num %= value
        return "".join(result)
