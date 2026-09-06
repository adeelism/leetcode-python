from solutions.sliding_window.p1695_maximum_erasure_value import Solution


def test_basic():
    assert Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17


def test_with_repeats():
    assert Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
