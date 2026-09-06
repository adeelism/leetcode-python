from solutions.two_pointers.p0027_remove_element import Solution


def test_example_1():
    nums = [3, 2, 2, 3]
    k = Solution().removeElement(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_example_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = Solution().removeElement(nums, 2)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]
