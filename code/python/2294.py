#https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0: 
            return len(set(nums))
        nums = sorted(list(set(nums)))
        start, res = nums[0], 1
        for num in nums:
            if num - start > k:
                res += 1
                start = num
        return res
