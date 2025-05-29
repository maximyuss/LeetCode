# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(node, level, par, count=1) -> int:
            if level < k:
                for child in graph[node]:
                    if child != par:
                        count += dfs(child, level + 1, node)
            return count

        m, n = len(edges1) + 1, len(edges2) + 1
        max_connection_graph2 = 0
        if k == 0: return [1] * m
        graph = [[] for _ in range(n)]
        for u, v in edges2:
            graph[u] += v,
            graph[v] += u,
        for node in range(n):
            max_connection_graph2 = max(max_connection_graph2, dfs(node, 1, -1))
        graph = [[] for _ in range(m)]
        for u, v in edges1:
            graph[u] += v,
            graph[v] += u,
        res = [0] * m
        for i in range(m):
            res[i] = dfs(i, 0, -1) + max_connection_graph2
        return res
