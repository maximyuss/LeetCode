# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        res = 0
        for num in nums:
            diff = k - num
            if diff in dict and dict[diff] > 0:
                dict[diff] -= 1
                res += 1
            else:
                dict[num] = dict.get(num, 0) + 1
        return res
