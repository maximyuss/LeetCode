# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder) - 1
        dq = deque()
        idx = 0
        for curr in preorder:
            node = TreeNode(curr)
            if dq:
                parent = dq[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            dq.append(node)
            while idx < n and postorder[idx] == dq[-1].val:
                dq.pop()
                idx += 1
        return dq[0]
