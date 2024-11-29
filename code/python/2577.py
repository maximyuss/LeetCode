# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        xy_end = (rows - 1, cols - 1)
        heap = [(0,0,0)]
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = 0
        while heap:
            time, x, y = heapq.heappop(heap)
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    ntime = time + 1
                    if grid[nx][ny] > ntime:
                        ntime = grid[nx][ny] + 1 - (grid[nx][ny] - time) % 2
                    if (nx, ny) == xy_end: return ntime
                    visited[nx][ny] = True
                    heapq.heappush(heap, (ntime, nx, ny))
        return -1
