# https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    # Dijkstra's Algorithm
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
                    new_effort = max(effort, abs(heights[x][y] - heights[x_new][y_new]))
                    if effort < efforts[x_new][y_new]:
                        efforts[x_new][y_new] = new_effort
                        heapq.heappush(pq, (new_effort, x_new, y_new))

    # Binary Search
    def minimumEffortPath(self, heights) -> int:
        def dfs(x, y, limit):
            if visited[x][y]: return
            visited[x][y] = True
            if x == n - 1 and y == m - 1: return
            for dx, dy in shifts:
                x_new, y_new = x + dx, y + dy
                if 0 <= x_new < n and 0 <= y_new < m:
                    new_effort = abs(heights[x][y] - heights[x_new][y_new])
                    if new_effort <= limit:
                        dfs(x_new, y_new, limit)

        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(heights), len(heights[0])
        l, r = 0, 1_000_000
        while l < r:
            mid = (l + r) // 2
            visited = [[False] * m for _ in range(n)]
            dfs(0, 0, mid)
            if visited[n - 1][m - 1]:
                r = mid
            else:
                l = mid + 1
        return l
