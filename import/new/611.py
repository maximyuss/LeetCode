# https://leetcode.com/problems/valid-triangle-number/
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 1, 1, -1):
            c = nums[i]
            if nums[0] + nums[1] > c:
                res += (i + 1) * (i) * (i - 1) // 6
                break
            if nums[i - 2] + nums[i - 1] < c:
                continue
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > c:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
