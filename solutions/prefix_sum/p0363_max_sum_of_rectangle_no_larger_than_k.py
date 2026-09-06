"""363. Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Find the largest sum of any sub-rectangle that does not exceed the bound k.

Approach: Fix a pair of top/bottom rows, compress the band into 1D column sums,
then use a sorted list of running prefixes with binary search to find the best
subarray sum not exceeding k.
Time:  O(rows^2 * cols * log cols)
Space: O(cols)
"""

from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        answer = float("-inf")
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sums[col] += matrix[bottom][col]
                best = self.max_sum_closest_to_k(col_sums, k)
                answer = max(answer, best)
                if answer == k:
                    return k
        return answer

    def max_sum_closest_to_k(self, nums: list[int], k: int) -> float:
        sorted_prefix = [0]
        max_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum += num
            required = current_sum - k
            idx = bisect_left(sorted_prefix, required)
            if idx < len(sorted_prefix):
                max_sum = max(max_sum, current_sum - sorted_prefix[idx])
            insort(sorted_prefix, current_sum)
        return max_sum
