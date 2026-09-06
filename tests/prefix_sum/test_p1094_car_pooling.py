from solutions.prefix_sum.p1094_car_pooling import Solution


def test_over_capacity():
    assert Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4) is False


def test_within_capacity():
    assert Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5) is True
