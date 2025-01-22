# https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dq, distances = deque(), [[-1] * n for _ in range(m)]
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell == 0:
                    dq.append((i, j))
                    distances[i][j] = 0
        while dq:
            x, y = dq.popleft()
            d = distances[x][y]
            for dx, dy in shifts:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and distances[nx][ny] == -1:
                    dq.append((nx, ny))
                    distances[nx][ny] = d + 1
        return distances
