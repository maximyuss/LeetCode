#https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem not in mp:
                mp[rem] = i
            elif i - mp[rem] > 1:
                return True
        return False
