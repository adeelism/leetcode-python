"""304. Range Sum Query 2D - Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/

Answer repeated queries for the sum of a rectangular sub-region of a fixed matrix.

Approach: Build a 2D prefix-sum grid using inclusion-exclusion, then answer each
region query in constant time with four lookups.
Time:  O(rows * cols) build, O(1) per query
Space: O(rows * cols)
"""


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] + self.prefix[r][c + 1] + self.prefix[r + 1][c] - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
