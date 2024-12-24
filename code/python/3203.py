# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find_diameter(tree, cur, parent):
            max_h1 = max_h2 = res_h = res_d = 0
            for neighbor in tree[cur]:
                if neighbor == parent: continue
                aspt_h, aspt_d = find_diameter(tree, neighbor, cur)
                aspt_h += 1
                if aspt_h > max_h1:
                    max_h2 = max_h1
                    max_h1 = aspt_h
                elif aspt_h > max_h2:
                    max_h2 = aspt_h
                res_h = max(res_h, aspt_h)
                res_d = max(res_d, aspt_d)
            return res_h, max(res_d, max_h1 + max_h2)

        tree1, tree2 = [[] for _ in range(len(edges1) + 1)], [[] for _ in range(len(edges2) + 1)]
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        d1 = max(find_diameter(tree1, 0, -1))
        d2 = max(find_diameter(tree2, 0, -1))
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
