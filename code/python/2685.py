# https://leetcode.com/problems/count-the-number-of-complete-components/
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False] * n
        res = 0
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            nodes = [i]
            for node in nodes:
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        nodes.append(neighbor)
                        visited[neighbor] = True
            target = len(nodes) - 1
            for node in nodes:
                if len(graph[node]) != target: break
            else:
                res += 1
        return res
