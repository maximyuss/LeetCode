# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        small = nsmallest(4, nums)
        big = nlargest(4, nums)
        min_diff = 10 ** 10 + 1
        for i in range(4):
            min_diff = min(min_diff, big[3 - i] - small[i])
        return min_diff
