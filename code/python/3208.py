# https://leetcode.com/problems/alternating-groups-ii/
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = cnt = 0
        for i in range(-k + 1, n):
            if colors[i] == colors[i - 1]:
                cnt = 1
            else:
                cnt += 1
            res += cnt >= k
        return res
