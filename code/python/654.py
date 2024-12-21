# https://leetcode.com/problems/maximum-binary-tree/
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            cur = TreeNode(num)
            while stack and num > stack[-1][0]:
                _, node = stack.pop()
                cur.left = node
            if stack and num < stack[-1][0]:
                stack[-1][1].right = cur
            stack.append((num, cur))
        return stack[0][1] if stack else None
