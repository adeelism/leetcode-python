from solutions.two_pointers.p0018_4sum import Solution


def test_example_1():
    result = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sorted(result) == sorted(expected)


def test_example_2():
    assert Solution().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
