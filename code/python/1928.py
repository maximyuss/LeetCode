# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for a, b, time in edges:
            if time > maxTime: continue
            graph[a].append((b, time))
            graph[b].append((a, time))
        times, costs = [float('inf')] * n, [float('inf')] * n
        times[0], costs[0] = 0, passingFees[0]
        pq = [(costs[0], times[0], 0)]
        while pq:
            cost, time, node = heapq.heappop(pq)
            if node == n - 1:
                return cost
            if cost > costs[node] and time > times[node]: continue
            for next, dt in graph[node]:
                new_time = time + dt
                new_cost = cost + passingFees[next]
                if new_time > maxTime: continue
                if new_cost < costs[next]:
                    costs[next] = new_cost
                    heapq.heappush(pq, (new_cost, new_time, next))
                elif new_time < times[next]:
                    times[next] = new_time
                    heapq.heappush(pq, (new_cost, new_time, next))
        return -1
