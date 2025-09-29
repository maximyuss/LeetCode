# https://leetcode.com/problems/climbing-stairs-ii/
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]  # dp[0] = 0
        last = [0, float('inf'), float('inf')]
        for j in range(1, n + 1):
            best = float('inf')
            for k in (1, 2, 3):
                if j - k >= 0:
                    prev = last[(j - k) % 3]
                    cost = prev + costs[j - 1] + k * k
                    if cost < best:
                        best = cost
            last[j % 3] = best
        return last[n % 3]
