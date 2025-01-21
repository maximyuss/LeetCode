# https://leetcode.com/problems/grid-game/
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum0 = res = sum(grid[0][1:])
        sum1 = 0
        for i in range(1, len(grid[0])):
            sum0 -= grid[0][i]
            sum1 += grid[1][i - 1]
            res_cur = max(sum0, sum1)
            if res_cur > res: break
            res = res_cur
        return res
