from solutions.prefix_sum.p0724_find_pivot_index import Solution


def test_basic():
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3


def test_none():
    assert Solution().pivotIndex([1, 2, 3]) == -1


def test_zero_index():
    assert Solution().pivotIndex([2, 1, -1]) == 0
