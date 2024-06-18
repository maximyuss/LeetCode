#https://leetcode.com/problems/ipo/
from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        pq = []
        idx = 0
        for i in range(k):
            while idx < n and projects[idx][0] <= w:
                heappush(pq, -projects[idx][1])
                idx += 1
            if not pq: break
            w -= heappop(pq)
        return w
