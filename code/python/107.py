# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, res = deque([root]), deque()
        while queue:
            res.appendleft([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[0].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return list(res)
