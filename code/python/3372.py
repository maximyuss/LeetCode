# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        def dfs(node, level, par, count=1) -> int:
            if level < k:
                for neighbor in graph[node]:
                    if neighbor != par:
                        count += dfs(neighbor, level + 1, node)
            return count

        m = len(edges1) + 1
        max_connection_graph2 = 0
        if k == 0:
            return [1] * m
        graph = build_graph(edges2)
        for node in range(len(edges2) + 1):
            max_connection_graph2 = max(max_connection_graph2, dfs(node, 1, -1))
        graph = build_graph(edges1)
        res = [0] * m
        for i in range(m):
            res[i] = dfs(i, 0, -1) + max_connection_graph2
        return res
