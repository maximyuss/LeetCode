# https://leetcode.com/problems/minimum-height-trees/
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        leafs = [i for i in range(len(graph)) if len(graph[i]) == 1]
        while len(graph) > 2:
            new_leafs = []
            for leaf in leafs:
                parent = graph[leaf][0]
                graph.pop(leaf)
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leafs.append(parent)
            leafs = new_leafs
        return list(graph.keys())
