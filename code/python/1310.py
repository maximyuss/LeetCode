# https://leetcode.com/problems/xor-queries-of-a-subarray/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        pref = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pref[i + 1] = pref[i] ^ arr[i]
        for l, r in queries:
            res.append(pref[l] ^ pref[r + 1])
        return res
