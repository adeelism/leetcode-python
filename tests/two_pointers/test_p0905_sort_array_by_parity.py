from solutions.two_pointers.p0905_sort_array_by_parity import Solution


def test_example_1():
    result = Solution().sortArrayByParity([3, 1, 2, 4])
    assert all(x % 2 == 0 for x in result[:2])
    assert all(x % 2 == 1 for x in result[2:])
    assert sorted(result) == [1, 2, 3, 4]


def test_example_2():
    result = Solution().sortArrayByParity([0])
    assert result == [0]
