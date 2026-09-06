from solutions.sliding_window.p0209_minimum_size_subarray_sum import Solution


def test_basic():
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2


def test_single_element_suffices():
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1


def test_impossible():
    assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
