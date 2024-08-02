# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_ones = sum(nums)
        n = len(nums)
        if count_ones == 0 or count_ones == n:
            return 0
        count_zeros = count_ones - sum(nums[:count_ones])
        res = count_zeros
        l = 0
        for r in range(count_ones, n + count_ones):
            count_zeros += nums[l] - nums[r % n]
            res = min(res, count_zeros)
            if res == 0:
                break
            l += 1
        return res
