# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxs = [0] * 82
        res = -1
        for num in nums:
            x, sum_d = num, 0
            while x:
                sum_d += x % 10
                x //= 10
            if maxs[sum_d] == 0:
                maxs[sum_d] = num
            else:
                res = max(res, maxs[sum_d] + num)
                if num > maxs[sum_d]:
                    maxs[sum_d] = num
        return res
