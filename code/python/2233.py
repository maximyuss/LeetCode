#https://leetcode.com/problems/maximum-product-after-k-increments/
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        modulo = int(1e9 + 7)
        res = idx = 1
        shift = 0
        if len(nums) == 1: return nums[0] + k
        nums.sort()
        while k > 0:
            if idx < len(nums):
                if nums[idx] >= nums[0]:
                    shift = min(nums[1] - nums[0] + 1, k)
                    nums[0] += shift
                    k -= shift
                    idx = 1
                if nums[idx] < nums[0]:
                    shift = min(nums[0] - nums[idx], k)
                    nums[idx] += shift
                    k -= shift
                    idx += 1
            else:
                idx = 1
        for e in nums:
            res *= e
            res %= modulo
        return res
