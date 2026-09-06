from solutions.arrays_hashing.p0001_two_sum import Solution


def test_basic():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_middle():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
