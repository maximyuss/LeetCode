#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def foo(index):
            if index == len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                foo(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        res = []
        foo(0)
        return res
