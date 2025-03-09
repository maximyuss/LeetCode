# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        lookup, res = {}, 0
        for i, num in enumerate(arr):
            lookup[num] = {}
            for j in range(i - 1, -1, -1):
                prev = arr[j]
                prev2 = num - prev
                if prev2 >= prev: break
                if prev2 in lookup:
                    lookup[num][prev] = lookup[prev].get(prev2, 2) + 1
                    res = max(res, lookup[num][prev])
        return res if res > 2 else 0
