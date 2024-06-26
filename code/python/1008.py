# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.idx = self.n = 0
        def build(arr, _max):
            if self.idx == self.n or arr[self.idx] > _max: return None
            root = TreeNode(arr[self.idx])
            self.idx+=1
            root.left = build(arr, root.val)
            root.right = build(arr, _max)
            return root

        self.n = len(preorder)
        return build(preorder, 1001)
