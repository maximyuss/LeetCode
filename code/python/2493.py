# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def is_bipartite(node):
            dq = deque([node])
            colors[node] = 1
            while dq:
                cur = dq.popleft()
                nodes.append(cur)
                for neighbour in graph[cur]:
                    if colors[neighbour] == colors[cur]:
                        return False
                    elif colors[neighbour] == 0:
                        dq.append(neighbour)
                        colors[neighbour] = -colors[cur]
            return True

        def count_levels(node) -> bool:
            dq = deque([(node, 1)])
            visited = [False] * n
            visited[node] = True
            res = 0
            while dq:
                cur, level = dq.popleft()
                res = max(res, level)
                for neighbor in graph[cur]:
                    if visited[neighbor]: continue
                    dq.append((neighbor, level + 1))
                    visited[neighbor] = True
            return res

        graph = [[] for _ in range(n)]
        colors = [0] * n
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        res = 0
        for i in range(n):
            if colors[i] == 0:
                nodes = []
                if not is_bipartite(i): return -1
                max_level = 0
                for node in nodes:
                    max_level = max(max_level, count_levels(node))
                res += max_level
        return res
