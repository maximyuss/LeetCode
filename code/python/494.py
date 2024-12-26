# https://leetcode.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diff = sum(nums) - target
        if diff < 0 or diff % 2 == 1: return 0

        d = {0:1}
        for num in nums:
            dp = {}
            for k, v in d.items():
                dp[k + num] = dp.get(k + num, 0) + v
                dp[k - num] = dp.get(k - num, 0) + v
            d = dp
        return d.get(target, 0)
