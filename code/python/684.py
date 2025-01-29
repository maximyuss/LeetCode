# https://leetcode.com/problems/redundant-connection/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return (u, v)
            parent[v_root] = u_root
            return None

        n = len(edges)
        parent = [i for i in range(n + 1)]
        res = None
        for u, v in edges:
            cycle_edge = union(u, v)
            if cycle_edge:
                if res is None or max(cycle_edge) > max(res):
                    res = cycle_edge
        return res
