# https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(heights), len(heights[0])
        efforts = [[float("inf")] * m for _ in range(n)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            effort, x, y = heapq.heappop(pq)
            if x == n - 1 and y == m - 1:
                return effort
            for dx, dy in shifts:
                x_new, y_new = x + dx, y + dy
                if 0 <= x_new < n and 0 <= y_new < m:
                    new_effort = abs(heights[x][y] - heights[x_new][y_new])
                    new_effort = max(effort, new_effort)
                    if effort < efforts[x_new][y_new]:
                        efforts[x_new][y_new] = new_effort
                        heapq.heappush(pq, (new_effort, x_new, y_new))
        return
