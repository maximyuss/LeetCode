# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        x_end, y_end = rows - 1, cols - 1
        dq = deque([(0, 0, grid[0][0])])
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        while dq:
            x, y, cost = dq.popleft()
            if (x, y) == (x_end, y_end): break
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 1:
                        dq.append((nx, ny, cost + 1))
                    else:
                        dq.appendleft((nx, ny, cost))
        return health > cost
