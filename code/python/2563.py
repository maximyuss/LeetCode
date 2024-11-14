# https://leetcode.com/problems/count-the-number-of-fair-pairs/
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1):
            l = bisect_left(nums, lower - nums[i], i + 1)
            r = bisect_right(nums, upper - nums[i], i + 1)
            res += r - l
        return res
