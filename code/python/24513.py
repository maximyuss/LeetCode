# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l_node, r_node, level):
            if not (l_node and r_node): return
            if level % 2:
                l_node.val, r_node.val = r_node.val, l_node.val
            dfs(l_node.left, r_node.right, level + 1)
            dfs(l_node.right, r_node.left, level + 1)

        dfs(root.left, root.right, 1)
        return root
