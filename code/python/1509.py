# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        arr = nsmallest(4, nums)
        tmp = nlargest(4, nums)
        for num in tmp[::-1]:
            if num > arr[3]:
                arr.append(num)
        res = 10 ** 10 + 1
        for l in range(4):
            r = len(arr) - 4 + l
            res = min(res, arr[r] - arr[l])
        return res
