from solutions.sliding_window.p2537_count_the_number_of_good_subarrays import Solution


def test_all_equal():
    assert Solution().countGood([1, 1, 1, 1, 1], 10) == 1


def test_mixed():
    assert Solution().countGood([3, 1, 4, 3, 2, 2, 4], 2) == 4
