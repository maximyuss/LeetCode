# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def dfs(x, y):
            if x == n - 1 and y == m - 1: return True
            if x > 0 or y > 0: grid[x][y] = 0
            if 0 <= y + 1 < m and grid[x][y + 1] == 1 and dfs(x, y + 1): return True
            if 0 <= x + 1 < n and grid[x + 1][y] == 1 and dfs(x + 1, y): return True
            return False
        
        n, m = len(grid), len(grid[0])
        if not dfs(0, 0): return True
        return not dfs(0, 0)
