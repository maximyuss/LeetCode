#https://leetcode.com/problems/most-profit-assigning-work/
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = idx = 0
        n = len(profit)
        diff_prof = list(zip(difficulty, profit))
        pq = []
        diff_prof.sort()
        worker.sort()
        for i in range(len(worker)):
            while idx < n and diff_prof[idx][0] <= worker[i]:
                heappush(pq, -diff_prof[idx][1])
                idx += 1
            if pq:
                res -= pq[0]
        return res
