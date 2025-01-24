# https://leetcode.com/problems/find-eventual-safe-states/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            state[node] = 1
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return False
                elif state[neighbor] == 0 and not dfs(neighbor):
                    return False
            state[node] = 2
            return True

        n = len(graph)
        state = [0] * n  # white, gray, black
        for i in range(n):
            if state[i] == 0:
                dfs(i)
        res = []
        for i in range(n):
            if state[i] == 2:
                res.append(i)
        return res
