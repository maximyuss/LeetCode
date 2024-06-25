# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def foo(root, _sum):
            if root is None: return
            foo(root.right, _sum)
            _sum[0] += root.val
            root.val = _sum[0]
            foo(root.left, _sum)

        _sum = [0]
        foo(root, _sum)
        return root
