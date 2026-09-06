"""1109. Corporate Flight Bookings
https://leetcode.com/problems/corporate-flight-bookings/

Compute the total seats booked on each of the n flights from a list of range bookings.

Approach: Apply each booking as a range update on a difference array, then take a
running prefix sum to recover the per-flight totals.
Time:  O(n + bookings)
Space: O(n)
"""


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        answer = [0] * n
        for i in range(n):
            if i == 0:
                answer[i] = diff[i]
            else:
                answer[i] = answer[i - 1] + diff[i]
        return answer
