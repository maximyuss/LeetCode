# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for a, b, time in edges:
            graph[a].append((b, time))
            graph[b].append((a, time))
        queue = deque([(0, 0, values[0], [0])])
        dp = [(-1, -1)] * n
        dp[0] = (values[0], 0)
        res = 0
        while queue:
            node, time, value, visited = queue.popleft()
            if node == 0:
                res = max(res, value)
            for next, dt in graph[node]:
                if time + dt > maxTime:
                    continue
                new_value = value
                if next not in visited:
                    new_value += values[next]
                if time + dt >= dp[next][1] and new_value < dp[next][0]:
                    continue
                queue.append((next, time + dt, new_value, visited + [next]))
                dp[next] = (new_value, time + dt)
        return res
