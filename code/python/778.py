# https://leetcode.com/problems/swim-in-rising-water/description/
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        dist = max(grid[0][0], grid[n - 1][m - 1])
        pq = [(dist, 0, 0)]
        visited = {(0, 0)}
        while pq:
            curr_dist, x, y = heapq.heappop(pq)
            dist = max(dist, curr_dist)
            if x == n - 1 and y == m - 1:
                return dist
            for dx, dy in shifts:
                x_new, y_new = x + dx, y + dy
                if 0 <= x_new < n and 0 <= y_new < m and (x_new, y_new) not in visited:
                    visited.add((x_new, y_new))
                    heapq.heappush(pq, (grid[x_new][y_new], x_new, y_new))
