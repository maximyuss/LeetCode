# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def solve(num, target):
            if target < 0 or num < target: return False
            if num == target: return True
            x, div = num, 10
            while x:
                y = num % div
                x //= 10
                if solve(x, target - y): return True
                div *= 10
            return False

        res = 0
        for i in range(1, n + 1):
            if solve(i * i, i):
                res += i * i
        return res
