from solutions.arrays_hashing.p1893_check_if_all_the_integers_in_a_range_are_covered import (
    Solution,
)


def test_covered():
    assert Solution().isCovered([[1, 2], [3, 4], [5, 6]], 2, 5) is True


def test_not_covered():
    assert Solution().isCovered([[1, 10], [10, 20]], 21, 21) is False
