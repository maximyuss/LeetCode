# https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        res = []
        while dq:
            len_level = len(dq)
            nodes = [0] * len_level
            for i in range(len_level):
                node = dq.popleft()
                nodes[i] = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(nodes)
        return res
