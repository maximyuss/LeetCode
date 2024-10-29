# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp_curr = [True] * rows
        for c in range(cols - 1):
            dp_next = [False] * rows
            for r in range(rows):
                if not dp_curr[r]: continue
                if r > 0: dp_next[r - 1] |= grid[r - 1][c + 1] > grid[r][c]
                dp_next[r] |= grid[r][c + 1] > grid[r][c]
                if r < rows - 1: dp_next[r + 1] |= grid[r + 1][c + 1] > grid[r][c]
            if not any(dp_next): return c
            dp_curr = dp_next
        else:
            return c + 1 if any(dp_curr) else c
