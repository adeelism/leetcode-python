from solutions.two_pointers.p0283_move_zeroes import Solution


def test_example_1():
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_example_2():
    nums = [0]
    Solution().moveZeroes(nums)
    assert nums == [0]
