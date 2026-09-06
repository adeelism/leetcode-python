from solutions.arrays_hashing.p0242_valid_anagram import Solution


def test_anagram():
    assert Solution().isAnagram("anagram", "nagaram") is True


def test_not_anagram():
    assert Solution().isAnagram("rat", "car") is False
