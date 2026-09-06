from solutions.sliding_window.p1493_longest_subarray_of_1s_after_deleting_one_element import (
    Solution,
)


def test_basic():
    assert Solution().longestSubarray([1, 1, 0, 1]) == 3


def test_mixed():
    assert Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5


def test_all_ones():
    assert Solution().longestSubarray([1, 1, 1]) == 2
