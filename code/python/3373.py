# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def calc_colors(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            colors = [-1] * n
            colors[0] = 0
            queue = deque([0])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
            return colors

        colors1 = calc_colors(edges1)
        colors2 = calc_colors(edges2)
        sum1, sum2 = sum(colors1), sum(colors2)
        cnt_colors1, cnt_colors2 = [len(colors1) - sum1, sum1], [len(colors2) - sum2, sum2]
        res = []
        for c in colors1:
            res.append(cnt_colors1[c] + max(cnt_colors2[0], cnt_colors2[1]))
        return res
