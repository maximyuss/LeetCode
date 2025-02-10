# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        shifts = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        x = y = 0
        dist_total = dist_prev = res = 0
        for c in s:
            x += shifts[c][0]
            y += shifts[c][1]
            dist_cur = abs(x) + abs(y)
            diff = dist_cur - dist_prev
            dist_prev = dist_cur
            if diff == -1 and k > 0:
                diff = 1
                k -= 1
            dist_total += diff
            if dist_total > res: res = dist_total
        return res
