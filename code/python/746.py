# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp1, dp2 = cost[0], cost[1]
        for i in range(2, n):
            curr = min(dp1, dp2) + cost[i]
            dp1, dp2 = dp2, curr
        return min(dp1, dp2)
