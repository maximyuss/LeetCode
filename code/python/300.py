# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        n = 0
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
                n += 1
            else:
                l, r = 0, n
                while l < r:
                    m = l + (r - l) // 2
                    if res[m] < nums[i]:
                        l = m + 1
                    else:
                        r = m
                res[l] = nums[i]
        return n + 1
