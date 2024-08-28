# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = 0
                for i in range(4):
                    check(row + shift[i][0],col + shift[i][1])

        shift = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    check(i, j)
                    count += 1
        return count
