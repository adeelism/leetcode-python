from solutions.sliding_window.p0424_longest_repeating_character_replacement import Solution


def test_basic():
    assert Solution().characterReplacement("ABAB", 2) == 4


def test_with_one_replacement():
    assert Solution().characterReplacement("AABABBA", 1) == 4
