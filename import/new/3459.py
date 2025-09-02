# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)
        m = len(grid[0])
        nv = [2, 2, 0] # Next expected value

        @functools.cache
        def helper(x, y, turned, dir):
            res = 1
            dx, dy = dirs[dir]
            if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                res = helper(x + dirs[dir][0], y + dirs[dir][1], turned, dir) + 1
            if not turned:
                dx, dy = dirs[(dir + 1) % 4]
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                    res = max(res, helper(x + dx, y + dy, True, (dir + 1) % 4) + 1)
            return res

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > res:
                            res = max(res, helper(i, j, False, d))
        return res
