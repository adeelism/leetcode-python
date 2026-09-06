from solutions.two_pointers.p0075_sort_colors import Solution


def test_example_1():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_example_2():
    nums = [2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 1, 2]
