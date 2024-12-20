# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def parse(s):
            res = deque()
            l = is_node = 0
            for r in range(len(s)):
                if is_node ^ (s[r] == '-'): continue
                if is_node:
                    val = int(s[l:r])
                else:
                    level = r - l
                if is_node:
                    res.append((level, val))
                is_node = not is_node
                l = r
            return res

        def dfs(node, parent_level):
            if not node or not nodes: return
            level, val = nodes[0]
            if level <= parent_level: return
            node.left = TreeNode(val)
            nodes.popleft()
            dfs(node.left, level)
            
            if not nodes: return
            level, val = nodes[0]
            if level <= parent_level: return
            node.right = TreeNode(val)
            nodes.popleft()
            dfs(node.right, level)

        nodes = parse(traversal + '-')
        root = TreeNode(nodes.popleft()[1])
        dfs(root, 0)
        return root
