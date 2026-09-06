from solutions.prefix_sum.p0525_contiguous_array import Solution


def test_basic():
    assert Solution().findMaxLength([0, 1]) == 2


def test_longer():
    assert Solution().findMaxLength([0, 1, 0]) == 2


def test_balanced():
    assert Solution().findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4
