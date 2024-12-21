# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grand):
            if not node: return 0
            nonlocal res
            if grand % 2 == 0: res += node.val
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)

        res = 0
        dfs(root, -1, -1)
        return res
