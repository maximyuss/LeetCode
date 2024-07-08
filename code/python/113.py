# https://leetcode.com/problems/path-sum-ii/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, sum: int):
            sum -= node.val
            if node.left is None and node.right is None:
                if sum == 0:
                    path.append(node.val)
                    res.append(path[:])
                    path.pop()
                return
            path.append(node.val)
            if node.left: dfs(node.left, path[:], sum)
            if node.right: dfs(node.right, path[:], sum)

        res = []
        if root is not None:
            dfs(root, [], targetSum)
        return res
