from solutions.binary_search.p0744_find_smallest_letter_greater_than_target import Solution


def test_greater():
    assert Solution().nextGreatestLetter(["c", "f", "j"], "a") == "c"


def test_middle():
    assert Solution().nextGreatestLetter(["c", "f", "j"], "c") == "f"


def test_wrap_around():
    assert Solution().nextGreatestLetter(["c", "f", "j"], "j") == "c"
