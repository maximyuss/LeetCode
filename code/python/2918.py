# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        cnt_zeros = [nums1.count(0), nums2.count(0)]
        min_sum = [sum(nums1) + cnt_zeros[0], sum(nums2) + cnt_zeros[1]]
        if min_sum[0] > min_sum[1] and not cnt_zeros[1] or \
            min_sum[1] > min_sum[0] and not cnt_zeros[0]:
            return -1
        return max(min_sum)
