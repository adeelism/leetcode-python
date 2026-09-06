from solutions.binary_search.p0852_peak_index_in_a_mountain_array import Solution


def test_short():
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1


def test_longer():
    assert Solution().peakIndexInMountainArray([0, 2, 3, 4, 5, 3, 1]) == 4
