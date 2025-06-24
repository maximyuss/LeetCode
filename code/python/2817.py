# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_nums = SortedList(nums[x:])
        n = len(nums)
        res = float('inf')
        for i in range(0, n-x):
            num = nums[i]
            idx = sorted_nums.bisect_left(num)
            if idx < len(sorted_nums):
                res = min(res, abs(sorted_nums[idx] - num))
            if idx > 0:
                res = min(res, abs(sorted_nums[idx - 1] - num))
            if res == 0:
                return 0
            sorted_nums.remove(nums[i+x])
        return res
