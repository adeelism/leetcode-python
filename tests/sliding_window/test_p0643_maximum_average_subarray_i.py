from solutions.sliding_window.p0643_maximum_average_subarray_i import Solution


def test_basic():
    assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75


def test_single():
    assert Solution().findMaxAverage([5], 1) == 5.0
