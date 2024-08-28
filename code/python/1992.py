# https://leetcode.com/problems/find-all-groups-of-farmland/
class Solution:
    area_max_row, area_max_col = 0, 0

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def check(row, col):
            if 0 <= row < rows and 0 <= col < cols and land[row][col] == 1:
                land[row][col] = 0
                if row >= self.area_max_row and col >= self.area_max_col:
                    self.area_max_row = row
                    self.area_max_col = col
                for i in range(4):
                    check(row + shift[i][0], col + shift[i][1])

        shift = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(land), len(land[0])
        res = []
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    self.area_max_row, self.area_max_col = row, col
                    check(row, col)
                    res.append([row, col, self.area_max_row, self.area_max_col])
        return res
