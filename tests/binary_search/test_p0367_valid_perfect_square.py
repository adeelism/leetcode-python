from solutions.binary_search.p0367_valid_perfect_square import Solution


def test_perfect():
    assert Solution().isPerfectSquare(16) is True


def test_not_perfect():
    assert Solution().isPerfectSquare(14) is False
