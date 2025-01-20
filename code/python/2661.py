# https://leetcode.com/problems/first-completely-painted-row-or-column/
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [n] * m, [m] * n
        nums_row, nums_col = [0] * (m * n + 1), [0] * (m * n + 1)
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                nums_row[num] = i
                nums_col[num] = j
        for i, num in enumerate(arr):
            rows[nums_row[num]] -= 1
            cols[nums_col[num]] -= 1
            if rows[nums_row[num]] == 0 or cols[nums_col[num]] == 0:
                return i
