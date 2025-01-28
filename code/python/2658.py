# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            res = grid[x][y]
            grid[x][y] = 0
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    res += dfs(nx, ny)
            return res

        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j))
        return res
