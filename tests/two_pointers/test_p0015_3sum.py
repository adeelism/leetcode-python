from solutions.two_pointers.p0015_3sum import Solution


def test_example_1():
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted(result) == sorted([[-1, -1, 2], [-1, 0, 1]])


def test_no_triplet():
    assert Solution().threeSum([0, 1, 1]) == []


def test_all_zeros():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
