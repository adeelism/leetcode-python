"""1876. Substrings of Size Three with Distinct Characters
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

Count the length-3 substrings of s whose three characters are all different.

Approach: Slide a fixed window of size 3 across s, counting it whenever its set of
characters has size 3.
Time:  O(n)
Space: O(1)
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        count = 0
        sub_string = ""
        if len(s) < k:
            return 0
        for i in range(k):
            sub_string += s[i]
        if len(set(sub_string)) == k:
            count += 1
        for i in range(k, len(s)):
            sub_string = sub_string[1:]
            sub_string += s[i]
            if len(set(sub_string)) == k:
                count += 1
        return count
