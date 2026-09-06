from solutions.prefix_sum.p0974_subarray_sums_divisible_by_k import Solution


def test_basic():
    assert Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7


def test_single():
    assert Solution().subarraysDivByK([5], 9) == 0
