from solutions.binary_search.p0069_sqrtx import Solution


def test_perfect_square():
    assert Solution().mySqrt(4) == 2


def test_floor():
    assert Solution().mySqrt(8) == 2


def test_small():
    assert Solution().mySqrt(1) == 1
