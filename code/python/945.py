#https://leetcode.com/problems/maximum-product-after-k-increments/
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = shift = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                shift = nums[i - 1] - nums[i] + 1
                nums[i] += shift
                res += shift
        return res
