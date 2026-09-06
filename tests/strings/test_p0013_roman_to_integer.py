from solutions.strings.p0013_roman_to_integer import Solution


def test_simple():
    assert Solution().romanToInt("III") == 3


def test_subtractive():
    assert Solution().romanToInt("MCMXCIV") == 1994


def test_mixed():
    assert Solution().romanToInt("LVIII") == 58
