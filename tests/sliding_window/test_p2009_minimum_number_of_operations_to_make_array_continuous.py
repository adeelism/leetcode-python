from solutions.sliding_window.p2009_minimum_number_of_operations_to_make_array_continuous import (
    Solution,
)


def test_already_continuous():
    assert Solution().minOperations([4, 2, 5, 3]) == 0


def test_one_operation():
    assert Solution().minOperations([1, 2, 3, 5, 6]) == 1


def test_all_far_apart():
    assert Solution().minOperations([1, 10, 100, 1000]) == 3
