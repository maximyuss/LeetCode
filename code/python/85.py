# https://leetcode.com/problems/maximal-rectangle/
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        cols = len(matrix[0])
        height = [0] * (cols + 1)
        for row in matrix:
            for i in range(cols):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            stack = []
            for i in range(cols + 1):
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
