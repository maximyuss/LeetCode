# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.gr = [[] for _ in range(n)]
        for start, end, cost in edges:
            self.gr[start].append((cost, end))

    def addEdge(self, edge: List[int]) -> None:
        start, end, cost = edge
        self.gr[start].append((cost, end))

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float('inf')] * len(self.gr)
        distances[node1] = 0
        pq = [(0, node1)]
        while pq:
            distance, start = heapq.heappop(pq)
            if start == node2: return distance
            if distance > distances[start]: continue
            for cost, neighbor in self.gr[start]:
                if distances[start] + cost < distances[neighbor]:
                    distances[neighbor] = distances[start] + cost
                    heapq.heappush(pq, (distances[neighbor], neighbor))
        return -1 if distances[node2] == float('inf') else distances[node2]
