from solutions.prefix_sum.p2574_left_and_right_sum_differences import Solution


def test_basic():
    assert Solution().leftRightDifference([10, 4, 8, 3]) == [15, 1, 11, 22]


def test_single():
    assert Solution().leftRightDifference([1]) == [0]
