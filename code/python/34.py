# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(is_upper=False):
            l, r = 0, n - 1
            x = target + 1 if is_upper else target
            while l < r:
                m = (l + r) // 2
                if nums[m] >= x:
                    r = m
                else:
                    l = m + 1
            if is_upper:
                if nums[l] != x - 1:
                    l -= 1
            else:
                if nums[l] != x:
                    l = -1
            return l

        n = len(nums)
        if n == 0: return [-1, -1]
        l = bin_search()
        if l == -1: return [-1, -1]
        r = bin_search(True)
        return [l, r]
