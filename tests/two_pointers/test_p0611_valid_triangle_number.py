from solutions.two_pointers.p0611_valid_triangle_number import Solution


def test_example_1():
    assert Solution().triangleNumber([2, 2, 3, 4]) == 3


def test_example_2():
    assert Solution().triangleNumber([4, 2, 3, 4]) == 4
