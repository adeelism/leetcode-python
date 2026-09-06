from solutions.sliding_window.p0930_binary_subarrays_with_sum import Solution


def test_basic():
    assert Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4


def test_all_zeros_goal_zero():
    assert Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15
