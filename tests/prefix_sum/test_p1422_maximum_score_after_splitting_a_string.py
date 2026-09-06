from solutions.prefix_sum.p1422_maximum_score_after_splitting_a_string import Solution


def test_basic():
    assert Solution().maxScore("011101") == 5


def test_all_shifts():
    assert Solution().maxScore("00111") == 5


def test_short():
    assert Solution().maxScore("1111") == 3
