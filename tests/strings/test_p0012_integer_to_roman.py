from solutions.strings.p0012_integer_to_roman import Solution


def test_small():
    assert Solution().intToRoman(3) == "III"


def test_subtractive():
    assert Solution().intToRoman(58) == "LVIII"


def test_large():
    assert Solution().intToRoman(3749) == "MMMDCCXLIX"
