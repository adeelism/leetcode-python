from solutions.sliding_window.p1876_substrings_of_size_three_with_distinct_characters import (
    Solution,
)


def test_basic():
    assert Solution().countGoodSubstrings("xyzzaz") == 1


def test_more():
    assert Solution().countGoodSubstrings("aababcabc") == 4
