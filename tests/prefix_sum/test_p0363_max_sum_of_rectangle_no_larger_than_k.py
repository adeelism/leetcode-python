from solutions.prefix_sum.p0363_max_sum_of_rectangle_no_larger_than_k import Solution


def test_basic():
    assert Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2) == 2


def test_single_cell():
    assert Solution().maxSumSubmatrix([[2, 2, -1]], 3) == 3
