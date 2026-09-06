from solutions.two_pointers.p0080_remove_duplicates_from_sorted_array_ii import Solution


def test_example_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = Solution().removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]


def test_example_2():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = Solution().removeDuplicates(nums)
    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]
