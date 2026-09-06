from solutions.two_pointers.p2529_maximum_count_of_positive_integer_and_negative_integer import (
    Solution,
)


def test_example_1():
    assert Solution().maximumCount([-2, -1, -1, 1, 2, 3]) == 3


def test_example_2():
    assert Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3


def test_example_3():
    assert Solution().maximumCount([5, 20, 66, 1314]) == 4
