# https://leetcode.com/problems/maximum-xor-of-subsequences/
class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0] * 31
        nums = Counter(nums)
        if len(nums) == 1 and nums[0] > 0: return 0
        for x in nums:
            while x:
                i = x.bit_length() - 1
                if not basis[i]:
                    basis[i] = x
                x ^= basis[i]
        res = 0
        for i in range(30, -1, -1):
            if (res ^ basis[i]) > res:
                res ^= basis[i]
        return res
