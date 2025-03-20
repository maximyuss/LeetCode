# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def find(node):
            parent = parents[node]
            while node != parent:
                parent, node = parents[parent], parent
            return parent

        def union(v1, v2, weight):
            p1, p2 = find(v1), find(v2)                        
            minCost[p1] &= weight & minCost[p2]
            minCost[p2] = minCost[p1]
            if p1 < p2:
                parents[p2] = p1 
            elif p1 > p2:
                parents[p1] = p2

        MAX_WEIGHT = 131071
        parents = [i for i in range(n)]
        minCost = [MAX_WEIGHT] * n
        for v1, v2, w in edges:
            union(v1, v2, w)          
        res = [-1] * len(query)
        for i, (v1, v2) in enumerate(query):
            p1, p2 = find(v1), find(v2)
            if p1 == p2 and minCost[p1] != MAX_WEIGHT:
                res[i] = (minCost[p1])
        return res
