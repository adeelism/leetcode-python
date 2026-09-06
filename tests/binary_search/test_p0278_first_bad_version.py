import solutions.binary_search.p0278_first_bad_version as m
from solutions.binary_search.p0278_first_bad_version import Solution


def test_first_bad():
    m._BAD = 4
    assert Solution().firstBadVersion(5) == 4


def test_all_bad():
    m._BAD = 1
    assert Solution().firstBadVersion(1) == 1
