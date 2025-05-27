# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        in_degree = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            in_degree[b] += 1
            graph[a].append(b)
        top_order = [i for i in range(n) if in_degree[i] == 0]
        i = 0
        while i < len(top_order):
            node = top_order[i]
            for neighbor in graph[node]:
                if in_degree[neighbor] == 1:
                    top_order.append(neighbor)
                in_degree[neighbor] -= 1
            i += 1
        if len(top_order) < n:
            return -1
        max_color = 0
        for color in set(colors):
            freq = [0] * n
            for node in reversed(top_order):
                cur_max = 0
                for neighbor in graph[node]:
                    cur_max = max(cur_max, freq[neighbor])
                freq[node] = cur_max + (color == colors[node])
                max_color = max(max_color, freq[node])
        return max_color
