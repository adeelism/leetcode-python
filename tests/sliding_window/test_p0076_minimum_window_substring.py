from solutions.sliding_window.p0076_minimum_window_substring import Solution


def test_basic():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"


def test_single_char():
    assert Solution().minWindow("a", "a") == "a"


def test_impossible():
    assert Solution().minWindow("a", "aa") == ""
