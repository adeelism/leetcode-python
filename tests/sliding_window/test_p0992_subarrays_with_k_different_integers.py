from solutions.sliding_window.p0992_subarrays_with_k_different_integers import Solution


def test_basic():
    assert Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7


def test_three_distinct():
    assert Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3
