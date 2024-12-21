# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, max_, min_):
            nonlocal res
            if not cur: return
            if cur.val > max_:
                max_ = cur.val
                if res < max_ - min_: res = max_ - min_
            elif cur.val < min_:
                min_ = cur.val
                if res < max_ - min_: res = max_ - min_
            dfs(cur.left, max_, min_)
            dfs(cur.right, max_, min_)

        res = 0
        dfs(root, root.val, root.val)
        return res
