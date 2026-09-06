from solutions.strings.p0014_longest_common_prefix import Solution


def test_common():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_none():
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
