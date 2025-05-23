# https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        def dfs(node: int, parent: int) -> list[int]:
            costs = [cost[node]]
            for neighbor in graph[node]:
                if neighbor != parent:
                    costs.extend(dfs(neighbor, node))
            costs.sort()
            if len(costs) < 3:
                res[node] = 1
            else:
                max_product = max(costs[0] * costs[1] * costs[-1], costs[-1] * costs[-2] * costs[-3])
                res[node] = max(0, max_product)                
            if len(costs) > 5:
                return [costs[0], costs[1], costs[-3], costs[-2], costs[-1]]
            return costs

        n = len(cost)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res = [0] * n
        dfs(0, -1)
        return res
