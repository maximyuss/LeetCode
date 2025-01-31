# https://leetcode.com/problems/making-a-large-island/
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def fill(x, y):
            grid[x][y] = -area
            areas[area] += 1
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 0:
                    fill(nx, ny)

        def check(x, y):
            res = 1
            neighbors = set()
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] < 0:
                    area = -grid[nx][ny]
                    if area in neighbors: continue
                    neighbors.add(area)
                    res += areas[area]
            return res

        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        areas = [0]
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    area += 1
                    areas.append(0)
                    fill(i, j)
        if area == 0: return 1
        if area == 1 and areas[1] >= (n * n - 1): return n * n
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    res = max(res, check(i, j))
        return res
