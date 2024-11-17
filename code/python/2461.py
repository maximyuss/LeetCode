# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k == 1: return max(nums)
        
        st = set()
        cur_sum = res = l = 0
        for r in range(len(nums)):
            while nums[r] in st:
                cur_sum -= nums[l]
                st.remove(nums[l])
                l += 1
            st.add(nums[r])
            cur_sum += nums[r]
            if len(st) == k:
                res = max(res, cur_sum)
                cur_sum -= nums[l]
                st.remove(nums[l])
                l += 1
        return res
