from solutions.prefix_sum.p0304_range_sum_query_2d_immutable import NumMatrix

MATRIX = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]


def test_sum_region():
    obj = NumMatrix(MATRIX)
    assert obj.sumRegion(2, 1, 4, 3) == 8
    assert obj.sumRegion(1, 1, 2, 2) == 11
    assert obj.sumRegion(1, 2, 2, 4) == 12
