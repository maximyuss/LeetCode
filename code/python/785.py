# https://leetcode.com/problems/is-graph-bipartite/
# DFS Solution:
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, color=1):
            colors[node] = color
            for neighbour in graph[node]:
                if colors[neighbour] == color or (colors[neighbour] == 0 and
                                                  not dfs(neighbour, -color)):
                    return False
            return True

        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0 and not dfs(i):
                return False
        return True

  # BFS Solution:
  '''
      def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for node in range(n):
            if colors[node] == 0:
                dq = deque([node])
                colors[node] = 1
                while dq:
                    curr = dq.popleft()
                    for neighbor in graph[curr]:
                        if colors[neighbor] == colors[curr]:
                            return False
                        elif colors[neighbor] == 0:
                            dq.append(neighbor)
                            colors[neighbor] = -colors[curr]
        return True
  '''
