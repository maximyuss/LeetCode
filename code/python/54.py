# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = 0, -1
        rows, cols = len(matrix), len(matrix[0])
        total = rows * cols
        res = []
        dir = 1
        while len(res) < total:
            for _ in range(cols):
                col += dir
                res.append(matrix[row][col])
            rows -= 1
            for _ in range(rows):
                row += dir
                res.append(matrix[row][col])
            cols -= 1
            dir = -dir
        return res
