# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            while nums[curr - 1] != curr:
                next = nums[curr - 1]
                nums[curr - 1] = curr
                curr = next
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
