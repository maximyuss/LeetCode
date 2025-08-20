// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
class Solution:
    def countMaxOrSubsets(self, nums):
        maxOR = 0
        for num in nums:
            maxOR |= num   
        return self.backtrack(nums, maxOR, 0, 0)

    def backtrack(self, nums, maxOR, index, currentOR):
        if index == len(nums):
            return 1 if currentOR == maxOR else 0
        if currentOR == maxOR:
            return 1 << (len(nums) - index)      
        include = self.backtrack(nums, maxOR, index + 1, currentOR | nums[index])
        exclude = self.backtrack(nums, maxOR, index + 1, currentOR)
        return include + exclude
