# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        _SHIFT = 20
        _MASK = 0xFFFFF
        
        dq = deque([root])
        res = 0
        while dq:
            len_level = len(dq)
            nodes = [0] * len_level
            for i in range(len_level):
                node = dq.popleft()
                nodes[i] = (node.val << _SHIFT) + i
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            nodes.sort()
            i = 0
            while i < len_level:
                pos = nodes[i] & _MASK
                if pos != i:
                    nodes[i], nodes[pos] = nodes[pos], nodes[i]
                    res += 1
                    i -= 1
                i += 1
        return res
