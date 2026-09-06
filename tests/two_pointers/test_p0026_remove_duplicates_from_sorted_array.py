from solutions.two_pointers.p0026_remove_duplicates_from_sorted_array import Solution


def test_example_1():
    nums = [1, 1, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]


def test_example_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]
