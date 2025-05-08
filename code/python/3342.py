# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        pq = [(0, 0, 0, 1)]
        moveTime[0][0] = -1
        while pq:
            t, x, y, dt = heappop(pq)
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    cell = moveTime[nx][ny]
                    if cell == -1:
                        continue
                    t_new = max(t, cell) + dt
                    if nx == n - 1 and ny == m - 1:
                        return t_new
                    heappush(pq, (t_new, nx, ny, dt ^ 3))
                    moveTime[nx][ny] = -1
