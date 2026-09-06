"""1094. Car Pooling
https://leetcode.com/problems/car-pooling/

Decide whether a car can serve all trips without ever exceeding its capacity.

Approach: Build a difference array over locations, adding passengers at pickup and
removing them at drop-off, then sweep the running occupancy against capacity.
Time:  O(n + max_location)
Space: O(max_location)
"""


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        n = max(toi for _, _, toi in trips)
        diff = [0] * (n + 1)
        for num_passengers, fromi, toi in trips:
            diff[fromi] += num_passengers
            diff[toi] -= num_passengers

        current_passengers = 0
        for i in range(n):
            current_passengers += diff[i]
            if current_passengers > capacity:
                return False
        return True
