from solutions.prefix_sum.p0303_range_sum_query_immutable import NumArray


def test_sum_range():
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3
