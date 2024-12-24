# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
class FindElements:
    def __recovery(self, val, node):
        self.store.add(val)
        if node.left: self.__recovery(2 * val + 1, node.left)
        if node.right: self.__recovery(2 * val + 2, node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.store = set()
        self.__recovery(0, root)

    def find(self, target: int) -> bool:
        return target in self.store
