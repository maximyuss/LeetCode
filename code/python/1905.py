# https://leetcode.com/problems/count-sub-islands/
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid2[row][col] > 0:
                grid2[row][col] = 0
                for i in range(4):
                    dfs(row + shift[i][0], col + shift[i][1])

        rows, cols = len(grid1), len(grid1[0])
        shift = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] > 0 and grid1[row][col] == 0:
                    dfs(row, col)
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] > 0:
                    dfs(row, col)
                    res += 1
        return res
