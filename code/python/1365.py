# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict = {}
        for i in range(len(nums) - 1, -1, -1):
            dict[sorted_nums[i]] = i
        return [dict[i] for i in nums]
