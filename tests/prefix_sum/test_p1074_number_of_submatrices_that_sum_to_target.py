from solutions.prefix_sum.p1074_number_of_submatrices_that_sum_to_target import Solution


def test_basic():
    assert Solution().numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0) == 4


def test_single_row():
    assert Solution().numSubmatrixSumTarget([[1, -1]], 0) == 1
