"""1074. Number of Submatrices That Sum to Target
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Count the sub-rectangles of a matrix whose elements sum exactly to target.

Approach: Fix a top/bottom row band and collapse it into 1D column sums, then
reduce each band to the "subarray sum equals target" count via a prefix map.
Time:  O(rows^2 * cols)
Space: O(cols)
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        answer = 0
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sums[col] += matrix[bottom][col]
                answer += self.count_subarrays(col_sums, target)
        return answer

    def count_subarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        count = 0
        freq = {}
        for j in range(len(prefix)):
            required = prefix[j] - target
            if required in freq:
                count += freq[required]
            freq[prefix[j]] = freq.get(prefix[j], 0) + 1
        return count
