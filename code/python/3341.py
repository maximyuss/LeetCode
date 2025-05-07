# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime) - 1, len(moveTime[0]) - 1
        pq = [(0, 0, 0)]
        visited = set((0, 0))
        while pq:
            time, x, y = heapq.heappop(pq)
            if x == n and y == m:
                return time
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= n and 0 <= ny <= m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (max(time, moveTime[nx][ny]) + 1, nx, ny))
