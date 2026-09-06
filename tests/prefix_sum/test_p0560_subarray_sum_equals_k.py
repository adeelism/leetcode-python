from solutions.prefix_sum.p0560_subarray_sum_equals_k import Solution


def test_basic():
    assert Solution().subarraySum([1, 1, 1], 2) == 2


def test_more():
    assert Solution().subarraySum([1, 2, 3], 3) == 2
