# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lst = []
        rem = grid[0][0] % x
        for row in grid:
            for num in row:
                if num % x != rem:
                    return -1
                lst.append(num)
        lst.sort()
        mid = lst[len(lst) // 2]
        res = 0
        for num in lst:
            res += abs(num - mid) // x
        return res
