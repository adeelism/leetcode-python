from solutions.sliding_window.p1343_number_of_sub_arrays_of_size_k_and_average_greater_than_or_equal_to_threshold import (  # noqa: E501
    Solution,
)


def test_basic():
    assert Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3


def test_many():
    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    assert Solution().numOfSubarrays(arr, 3, 5) == 6
