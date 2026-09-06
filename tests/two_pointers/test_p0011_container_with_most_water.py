from solutions.two_pointers.p0011_container_with_most_water import Solution


def test_example_1():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    assert Solution().maxArea([1, 1]) == 1
