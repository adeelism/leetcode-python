from solutions.prefix_sum.p1524_number_of_sub_arrays_with_odd_sum import Solution


def test_basic():
    assert Solution().numOfSubarrays([1, 3, 5]) == 4


def test_all_even():
    assert Solution().numOfSubarrays([2, 4, 6]) == 0
