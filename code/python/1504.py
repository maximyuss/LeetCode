# https://leetcode.com/problems/count-submatrices-with-all-ones/
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0])
        res = 0
        for row in mat:
            S, stack = 0, []
            for i, cell in enumerate(row):
                if cell == 0:
                    S = heights[i] = 0
                    stack.clear()
                    continue
                cur_height = heights[i] + 1
                width = 0
                while stack and stack[-1][0] >= cur_height:
                    h, w = stack.pop()
                    S -= h * w
                    width += w
                width += 1
                heights[i] = cur_height
                stack.append((cur_height, width))
                S += cur_height * width
                res += S
        return res
