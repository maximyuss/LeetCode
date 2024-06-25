# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def foo(root):
            if (root == None): return 0, 0
            r_sum, r_cnt = foo(root.right)
            l_sum, l_cnt = foo(root.left)
            _sum = r_sum + l_sum + root.val
            _count = r_cnt + l_cnt + 1
            if root.val == _sum // _count:
                self.res += 1
            return _sum, _count

        foo(root)
        return self.res
