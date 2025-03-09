# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            t = 0
            for pile in piles:
                t += (pile - 1) // m + 1
            if t > h:
                l = m + 1
            else:
                r = m
        return l
