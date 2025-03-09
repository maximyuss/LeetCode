# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(target):
            day = 1
            load = 0
            for w in weights:
                load += w
                if load > target:
                    day += 1
                    load = w
            return day <= days
            
        if days == 1: return sum(weights)
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
