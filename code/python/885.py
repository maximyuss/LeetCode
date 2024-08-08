# https://leetcode.com/problems/spiral-matrix-iii/
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        shift_idx = 0
        row, col = rStart, cStart
        res = []
        steps = 1
        while len(res) < (rows * cols):
            for _ in range(2):
                for _ in range(steps):
                    if (-1 < row < rows) and (-1 < col < cols):
                        res.append([row, col])
                    row += shifts[shift_idx][0]
                    col += shifts[shift_idx][1]
                shift_idx = (shift_idx + 1) % 4
            steps += 1
        return res
