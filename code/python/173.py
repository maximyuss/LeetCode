# https://leetcode.com/problems/binary-search-tree-iterator/
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
