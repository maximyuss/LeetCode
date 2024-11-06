# https://leetcode.com/problems/find-if-array-can-be-sorted/
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n, l, prev_max = len(nums), 0, -1
        while l < n - 1:
            r = l + 1
            curr_max = curr_min = nums[l]
            while r < n and nums[l].bit_count() == nums[r].bit_count():
                curr_min, curr_max = min(curr_min, nums[r]), max(curr_max, nums[r])
                r += 1
            if prev_max > curr_min or r < n and curr_max > nums[r]: return False
            l, prev_max = r, curr_max
        return True
      
'''
# Second solution

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = curr_min = curr_max = prev_cnt = 0
        for n in nums:
            curr_cnt = n.bit_count()
            if prev_cnt == curr_cnt:
                curr_min = min(curr_min, n)
                curr_max = max(curr_max, n)
            elif curr_min < prev_max:
                return False
            else:
                prev_max = curr_max
                curr_min = curr_max = n
                prev_cnt = curr_cnt
        return curr_min >= prev_max
'''
