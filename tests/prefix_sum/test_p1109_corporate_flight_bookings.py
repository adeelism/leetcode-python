from solutions.prefix_sum.p1109_corporate_flight_bookings import Solution


def test_basic():
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    assert Solution().corpFlightBookings(bookings, 5) == [10, 55, 45, 25, 25]


def test_two_flights():
    assert Solution().corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25]
