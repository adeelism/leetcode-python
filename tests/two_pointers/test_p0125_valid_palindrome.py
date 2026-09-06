from solutions.two_pointers.p0125_valid_palindrome import Solution


def test_example_1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True


def test_example_2():
    assert Solution().isPalindrome("race a car") is False


def test_empty_after_filter():
    assert Solution().isPalindrome(" ") is True
