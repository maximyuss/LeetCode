# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = suff = 1
        res = [0] * n
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        return res
