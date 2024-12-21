# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(cur: int, parent: int) -> int:
            total = values[cur]
            for node in graph[cur]:
                if node != parent:
                    total += dfs(node, cur)
            nonlocal res
            total %= k
            res += (total == 0)
            return total

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        dfs(0, -1)
        return res
