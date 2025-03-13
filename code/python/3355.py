# https://leetcode.com/problems/zero-array-transformation-i/
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        acc = 0
        for i, num in enumerate(nums):
            acc += diff[i]
            if num > acc:
                return False
        return True
