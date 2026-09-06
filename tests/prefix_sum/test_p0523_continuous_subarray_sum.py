from solutions.prefix_sum.p0523_continuous_subarray_sum import Solution


def test_true():
    assert Solution().checkSubarraySum([23, 2, 4, 6, 7], 6) is True


def test_true_full():
    assert Solution().checkSubarraySum([23, 2, 6, 4, 7], 6) is True


def test_false():
    assert Solution().checkSubarraySum([23, 2, 6, 4, 7], 13) is False
