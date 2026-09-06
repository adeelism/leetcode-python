from solutions.prefix_sum.p1480_running_sum_of_1d_array import Solution


def test_basic():
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_ones():
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
