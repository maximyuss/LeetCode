# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def calc_distances(node: int) -> list[int]:
            distances = [MAX] * len(edges)
            dist = 0
            while node != -1 and distances[node] == MAX:
                distances[node] = dist
                dist += 1
                node = edges[node]
            return distances

        MAX = 10**6
        if node1 == node2: return node1
        dist1, dist2 = calc_distances(node1), calc_distances(node2)
        res_idx, res_dist = -1, MAX
        for i in range(len(edges)):
            dist = max(dist1[i], dist2[i])
            if dist < res_dist:
                res_idx = i
                res_dist = dist
        return res_idx
