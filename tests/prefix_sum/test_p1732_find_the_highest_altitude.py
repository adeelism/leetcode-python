from solutions.prefix_sum.p1732_find_the_highest_altitude import Solution


def test_basic():
    assert Solution().largestAltitude([-5, 1, 5, 0, -7]) == 1


def test_all_negative():
    assert Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
