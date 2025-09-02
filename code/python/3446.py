# https://leetcode.com/problems/sort-matrix-by-diagonals/
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(1, n - 1):
            buff = [0] * (n - i)
            for j in range(n - i):
                buff[j] = grid[j][i + j]
            buff.sort()
            for j in range(n - i):
                grid[j][i + j] = buff[j]
        for i in range(n - 1):
            buff = [0] * (n - i)
            for j in range(n - i):
                buff[j] = grid[i + j][j]
            buff.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = buff[j]
        return grid
