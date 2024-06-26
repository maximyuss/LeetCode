# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []

        def inorderTraversal(root):
            if not root: return
            inorderTraversal(root.left)
            self.arr.append(root.val)
            inorderTraversal(root.right)

        def sortedArrayToBST(l, r):
            if r < l: return None
            mid = l + (r - l) // 2
            node = TreeNode((self.arr[mid]))
            node.left = sortedArrayToBST(l, mid - 1)
            node.right = sortedArrayToBST(mid + 1, r)
            return node

        inorderTraversal(root)
        return sortedArrayToBST(0, len(self.arr) - 1)
