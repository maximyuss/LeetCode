# https://leetcode.com/problems/russian-doll-envelopes/
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        res = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            h = envelopes[i][1]
            if h > res[-1]:
                res.append(h)
            else:
                l, r = 0, len(res) - 1
                while l < r:
                    m = (l + r) // 2
                    if res[m] < h:
                        l = m + 1
                    else:
                        r = m
                res[l] = h
        return len(res)
