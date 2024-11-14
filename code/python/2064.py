# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l < r:
            m = (l + r) // 2
            if sum((q + m - 1) // m for q in quantities) <= n:
                r = m
            else:
                l = m + 1
        return l
