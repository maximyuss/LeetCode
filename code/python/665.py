# https://leetcode.com/problems/non-decreasing-array/
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_changed = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]: continue
            if is_changed: return False
            if not(i == 0 or nums[i - 1] <= nums[i + 1]):
                nums[i + 1] = nums[i]
            is_changed = True
        return True
