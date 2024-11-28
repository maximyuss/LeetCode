# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 2: return rows + cols - 2
        shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        x_end, y_end = rows - 1, cols - 1
        dq = deque()
        dq.append((0, 0, k, 0))
        visited = [[-1 for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = k
        while dq:
            x, y, rem, steps = dq.popleft()
            if (x, y) == (x_end, y_end): return steps
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    next_k = rem - grid[nx][ny]
                    if next_k < 0: continue
                    if visited[nx][ny] >= next_k:
                        continue
                    visited[nx][ny] = next_k
                    dq.append((nx, ny, next_k, steps + 1))
        return -1
