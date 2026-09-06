from solutions.math.p1266_minimum_time_visiting_all_points import Solution


def test_example_one():
    assert Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]) == 7


def test_example_two():
    assert Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]) == 5
