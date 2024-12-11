# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, k2 = 0, k * 2
        for r in range(len(nums)):
            if nums[r] - nums[l] > k2:
                l += 1
        return r - l + 1
