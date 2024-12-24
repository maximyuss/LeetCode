# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        def dfs(cur):
            total, diff_w = 0, deque()
            for neighbor, weight in graph[cur].items():
                graph[neighbor].pop(cur)
                without_edge, with_edge = dfs(neighbor)
                with_edge += weight
                if without_edge < with_edge:
                    total += with_edge
                    diff_w.append(without_edge - with_edge)
                else:
                    total += without_edge
            if len(diff_w) < k:
                return total, total
            diff_w = sorted(diff_w)
            total += sum(diff_w[k:])
            return total, total + diff_w[k - 1]

        graph = [{} for _ in range(len(edges) + 1)]
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        return dfs(0)[0]
