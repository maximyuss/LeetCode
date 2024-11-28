# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(n)}
        for i in range(1, n):
            edges[i - 1].append(i)
        distances = list(range(n))
        res = [1] * len(queries)
        for i in range(len(queries)):
            node1, node2 = queries[i]
            edges[node1].append(node2)
            distances[node2] = min(distances[node2], distances[node1] + 1)
            queue = [(distances[node2], node2)]
            while queue:
                dist, node = heapq.heappop(queue)
                if distances[node] < dist:
                    continue
                for next_node in edges[node]:
                    next_dist = dist + 1
                    if distances[next_node] <= next_dist:
                        continue
                    distances[next_node] = next_dist
                    heapq.heappush(queue, (next_dist, next_node))
            res[i] = distances[-1]
            if res[i] == 1: break
        return res
