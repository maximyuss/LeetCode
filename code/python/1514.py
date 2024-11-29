# https://leetcode.com/problems/path-with-maximum-probability/
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        probability = [0.0] * n
        probability[start_node] = 1.0
        pq = [(-1.0, start_node)]
        while pq:
            prob, node = heapq.heappop(pq)
            prob *= -1  # Get the actual probability
            if node == end_node: return prob
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > probability[neighbor]:
                    probability[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        return 0.0
