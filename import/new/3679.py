# https://leetcode.com/problems/minimum-discards-to-balance-inventory/
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        max_, res = max(arrivals), 0
        count = [0] * (max_ + 1)
        for idx, type_ in enumerate(arrivals):
            if idx >= w:
                left = arrivals[idx - w]
                count[left] -= left != 0
            if count[type_] == m:
                res += 1
                arrivals[idx] = 0
            else:
                count[type_] += 1
        return res
