from solutions.sliding_window.p1004_max_consecutive_ones_iii import Solution


def test_basic():
    assert Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6


def test_larger():
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    assert Solution().longestOnes(nums, 3) == 10
