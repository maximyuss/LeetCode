# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 1
        shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row, col in guards:
            for dr, dc in shifts:
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1:
                        break
                    if grid[r][c] == 0:
                        grid[r][c] = 2
                    r += dr
                    c += dc
        res = sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)
        return res
