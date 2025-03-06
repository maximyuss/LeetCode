# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r and nums[l] > nums[r]:
            m = l + (r - l) // 2
            if nums[m] < nums[l]:
                r = m
            else:
                l = m + 1
        return nums[l]
