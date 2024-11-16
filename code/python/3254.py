# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        n, k = len(nums), k - 1
        res = [-1] * (n - k)
        i, idx, cnt = 1, 0, k
        while i < n:
            if nums[i] == nums[i - 1] + 1:
                if cnt == 1:
                    res[idx] = nums[i]
                    idx += 1
                else:
                    cnt -= 1
            else:
                cnt, idx = k, i
            i += 1
        return res
