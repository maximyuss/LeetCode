# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    rows[i] -= 1
                    cols[j] -= 1
                else:
                    rows[i] += 1
                    cols[j] += 1
        for i in range(m):
            for j in range(n):
                grid[i][j] = rows[i] + cols[j]
        return grid
