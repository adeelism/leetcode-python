from solutions.sliding_window.p0003_longest_substring_without_repeating_characters import (
    Solution,
)


def test_basic():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_all_same():
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test_mixed_and_empty():
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
