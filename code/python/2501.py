# https://leetcode.com/problems/longest-square-streak-in-an-array/
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        calc = {}
        res = 0
        for num in nums:
            if num in calc:
                res = max(res, calc[num] + 1)
                calc[num * num] = calc[num] + 1
            else:
                calc[num * num] = 1
        return res if res > 1 else -1
