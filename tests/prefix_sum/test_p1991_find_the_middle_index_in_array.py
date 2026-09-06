from solutions.prefix_sum.p1991_find_the_middle_index_in_array import Solution


def test_basic():
    assert Solution().findMiddleIndex([2, 3, -1, 8, 4]) == 3


def test_first_index():
    assert Solution().findMiddleIndex([1, -1, 4]) == 2


def test_none():
    assert Solution().findMiddleIndex([2, 5]) == -1
