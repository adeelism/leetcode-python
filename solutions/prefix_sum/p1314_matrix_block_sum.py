"""1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Build a matrix where each cell holds the sum of all cells within k steps of it.

Approach: Precompute a 2D prefix sum, then for every cell clamp the k-radius block
to the grid bounds and read its sum in constant time via inclusion-exclusion.
Time:  O(rows * cols)
Space: O(rows * cols)
"""


class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )

        def get_sum(r1: int, r2: int, c1: int, c2: int) -> int:
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

        answer = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(rows - 1, i + k)
                c2 = min(cols - 1, j + k)
                answer[i][j] = get_sum(r1, r2, c1, c2)
        return answer
