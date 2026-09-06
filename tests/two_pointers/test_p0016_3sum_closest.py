from solutions.two_pointers.p0016_3sum_closest import Solution


def test_example_1():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2


def test_example_2():
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
