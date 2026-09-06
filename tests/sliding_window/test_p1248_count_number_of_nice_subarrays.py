from solutions.sliding_window.p1248_count_number_of_nice_subarrays import Solution


def test_basic():
    assert Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2


def test_none():
    assert Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2], 2) == 0
