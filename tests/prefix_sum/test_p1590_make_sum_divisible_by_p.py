from solutions.prefix_sum.p1590_make_sum_divisible_by_p import Solution


def test_basic():
    assert Solution().minSubarray([3, 1, 4, 2], 6) == 1


def test_no_removal_needed():
    assert Solution().minSubarray([6, 3, 5, 2], 9) == 2


def test_impossible():
    assert Solution().minSubarray([1, 2, 3], 3) == 0
