from solutions.prefix_sum.p1314_matrix_block_sum import Solution


def test_k1():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().matrixBlockSum(mat, 1) == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]


def test_k2():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().matrixBlockSum(mat, 2) == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
