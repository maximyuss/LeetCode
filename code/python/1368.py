# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(grid), len(grid[0])
        dist = [[float("inf")] * m for _ in range(n)]
        dist[0][0] = 0
        dq = deque([(0, 0)])
        while dq:
            r, c = dq.popleft()
            for shift, (dx, dy) in enumerate(shifts):
                r_new, c_new = r + dx, c + dy
                cost = 0 if grid[r][c] == shift + 1 else 1
                if (0 <= r_new < n and 0 <= c_new < m and dist[r][c] + cost < dist[r_new][c_new]):
                    dist[r_new][c_new] = dist[r][c] + cost
                    if cost == 1:
                        dq.append((r_new, c_new))
                    else:
                        dq.appendleft((r_new, c_new))
        return dist[-1][-1]
