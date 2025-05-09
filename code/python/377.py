# https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        n = len(nums)
        for cur_sum in range(1, target + 1):
            for num in nums:
                if cur_sum - num >= 0:
                    dp[cur_sum] += dp[cur_sum - num]
        return dp[target]
