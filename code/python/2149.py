# https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        ptr_pos, ptr_neg = 0, 1
        for num in nums:
            if num > 0:
                res[ptr_pos] = num
                ptr_pos += 2
            else:
                res[ptr_neg] = num
                ptr_neg += 2
        return res
