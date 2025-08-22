# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        y0 = next((i for i in range(n) if 1 in grid[i]), None)
        if y0 is None: return 0
        y1 = next((i for i in range(n - 1, -1, -1) if 1 in grid[i]), None)
        x0 = next((j for j in range(m) if any(grid[i][j] for i in range(y0, y1 + 1))), None)
        x1 = next((j for j in range(m - 1, -1, -1) if any(grid[i][j] for i in range(y0, y1 + 1))), None)
        return (x1 - x0 + 1) * (y1 - y0 + 1)
