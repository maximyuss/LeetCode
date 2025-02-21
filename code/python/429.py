# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        queue = deque([root])
        res = []
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[-1].append(node.val)
                queue.extend(node.children)
        return res
