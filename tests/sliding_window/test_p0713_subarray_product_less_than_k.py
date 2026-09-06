from solutions.sliding_window.p0713_subarray_product_less_than_k import Solution


def test_basic():
    assert Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8


def test_k_too_small():
    assert Solution().numSubarrayProductLessThanK([1, 2, 3], 0) == 0
