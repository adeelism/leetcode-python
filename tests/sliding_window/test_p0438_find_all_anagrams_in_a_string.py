from solutions.sliding_window.p0438_find_all_anagrams_in_a_string import Solution


def test_basic():
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]


def test_overlapping():
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]


def test_pattern_longer_than_text():
    assert Solution().findAnagrams("a", "abc") == []
