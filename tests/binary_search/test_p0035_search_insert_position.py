from solutions.binary_search.p0035_search_insert_position import Solution


def test_found():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2


def test_insert_middle():
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1


def test_insert_end():
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
