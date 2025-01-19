# https://leetcode.com/problems/trapping-rain-water-ii/
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3: return 0
        visited = [[False] * n for _ in range(m)]
        cnt = (m - 2) * (n - 2)
        pq = []
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in [0, m - 1]:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    res += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
                    cnt -= 1
            if cnt == 0: break
        return res
