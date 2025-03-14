# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, sum(candies) // k
        while l < r:
            m = l + (r - l + 1) // 2
            # Divide the candies between the children
            cnt = k
            is_posible = False
            for candy in candies:
                cnt -= candy // m
                if cnt <=0:
                    is_posible = True
                    break
            if is_posible:
                l = m
            else:
                r = m - 1
        return l
