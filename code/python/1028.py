# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(i=0, depth=0):
            if i == n or traversal[i:i + depth] != "-" * depth:
                return None, i
            i += depth
            j = i
            while j < n and traversal[j] != "-":
                j += 1
            node = TreeNode(int(traversal[i:j]))
            node.left, i = dfs(j, depth + 1)
            node.right, i = dfs(i, depth + 1)
            return node, i

        n = len(traversal)
        return dfs()[0]
