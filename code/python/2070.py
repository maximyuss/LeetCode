# https://leetcode.com/problems/most-beautiful-item-for-each-query/
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n_i, n_q = len(items), len(queries)
        items.sort(key=lambda x: x[0])
        pref = [0] * n_i
        pref[0] = items[0][1]
        for i in range(1, n_i):
            pref[i] = max(pref[i - 1], items[i][1])
        res, n_i = [0] * len(queries), n_i - 1
        for i in range(0, n_q):
            if queries[i] < items[0][0]:
                res[i] = 0
            elif queries[i] > items[n_i][0]:
                res[i] = pref[n_i]
            else:
                l, r = 0, n_i
                while l < r:
                    m = (l + r + 1) // 2
                    if queries[i] < items[m][0]:
                        r = m - 1
                    else:
                        l = m
                res[i] = pref[l]
        return res
