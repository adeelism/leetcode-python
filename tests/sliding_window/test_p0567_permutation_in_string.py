from solutions.sliding_window.p0567_permutation_in_string import Solution


def test_present():
    assert Solution().checkInclusion("ab", "eidbaooo") is True


def test_absent():
    assert Solution().checkInclusion("ab", "eidboaoo") is False
