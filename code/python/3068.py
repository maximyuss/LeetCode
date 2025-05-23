# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = cnt_good = 0
        pos_min, neg_max = float("inf"), float("-inf")
        for num in nums:
            total += num
            gain = (num ^ k) - num
            if gain > 0:
                pos_min = min(pos_min, gain)
                total += gain
                cnt_good += 1
            else:
                neg_max = max(neg_max, gain)
        if cnt_good % 2 == 0:
            return total
        return max(total - pos_min, total + neg_max)
