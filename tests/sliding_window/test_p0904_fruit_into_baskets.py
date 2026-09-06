from solutions.sliding_window.p0904_fruit_into_baskets import Solution


def test_basic():
    assert Solution().totalFruit([1, 2, 1]) == 3


def test_three_types():
    assert Solution().totalFruit([0, 1, 2, 2]) == 3


def test_longer_window():
    assert Solution().totalFruit([1, 2, 3, 2, 2]) == 4
