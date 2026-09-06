from solutions.prefix_sum.p0238_product_of_array_except_self import Solution


def test_basic():
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_with_zero():
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
