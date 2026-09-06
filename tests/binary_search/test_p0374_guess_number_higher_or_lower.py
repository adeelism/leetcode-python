import solutions.binary_search.p0374_guess_number_higher_or_lower as m
from solutions.binary_search.p0374_guess_number_higher_or_lower import Solution


def test_guess():
    m._PICK = 6
    assert Solution().guessNumber(10) == 6


def test_single():
    m._PICK = 1
    assert Solution().guessNumber(1) == 1
