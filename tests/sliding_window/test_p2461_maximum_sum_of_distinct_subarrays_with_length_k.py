from solutions.sliding_window.p2461_maximum_sum_of_distinct_subarrays_with_length_k import (
    Solution,
)


def test_basic():
    assert Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15


def test_no_distinct_window():
    assert Solution().maximumSubarraySum([4, 4, 4], 3) == 0
