# https://leetcode.com/problems/continuous-subarrays/
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = r = res = 0
        cur_min = cur_max = nums[0]
        for r in range(len(nums)):
            cur_min = min(cur_min, nums[r])
            cur_max = max(cur_max, nums[r])
            if cur_max - cur_min > 2:
                window_len = r - l
                res += window_len * (window_len + 1) // 2
                l = r
                cur_min = cur_max = nums[r]
                while l > 0 and abs(nums[r] - nums[l - 1]) <= 2:
                    l -= 1
                    cur_min = min(cur_min, nums[l])
                    cur_max = max(cur_max, nums[l])
                if l < r:
                    window_len = r - l
                    res -= window_len * (window_len + 1) // 2
        window_len = r - l + 1
        res += window_len * (window_len + 1) // 2
        return res
