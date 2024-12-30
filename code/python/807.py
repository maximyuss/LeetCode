# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        rows_top = [max(grid[i]) for i in range(n)]
        cols_top = [0] * n
        for r in range(n):
            for c in range(n):
                cols_top[c] = max(cols_top[c], grid[r][c])
        res = 0
        for r in range(n):
            for c in range(n):
                res += max(0, min(rows_top[r], cols_top[c]) - grid[r][c])
        return res
