# https://leetcode.com/problems/valid-arrangement-of-pairs/
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Eulerian path
        def dfs(cur):
            while graph[cur]:
                next = graph[cur].pop()
                dfs(next)
                path.append((cur, next))

        graph = defaultdict(list)
        in_out_degree = defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            in_out_degree[u] += 1
            in_out_degree[v] -= 1
        # Selection of the starting node
        start_node = pairs[0][0]
        for node in in_out_degree:
            if in_out_degree[node] == 1:
                start_node = node
                break
        path = []
        dfs(start_node)
        return path[::-1]
