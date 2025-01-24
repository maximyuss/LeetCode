# https://leetcode.com/problems/build-a-matrix-with-conditions/
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions: List[List[int]]) -> List[int]:
            order = []
            graph = [[] for _ in range(k + 1)]
            in_degrees = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                in_degrees[v] += 1
            dq = deque()
            for i in range(1, k + 1):
                if in_degrees[i] == 0:
                    dq.append(i)
            while dq:
                u = dq.popleft()
                order.append(u)
                for v in graph[u]:
                    in_degrees[v] -= 1
                    if in_degrees[v] == 0:
                        dq.append(v)
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        if not row_order: return []
        col_order = topo_sort(colConditions)
        if not col_order: return []

        res = [[0] * k for _ in range(k)]
        row_index = [0] * (k + 1)
        for i, node in enumerate(row_order):
            row_index[node] = i
        for j, node in enumerate(col_order):
            res[row_index[node]][j] = node
        return res
