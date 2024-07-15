# https://leetcode.com/problems/create-binary-tree-from-descriptions/

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def get_node(val) -> TreeNode:
            if val in nodes:
                res = nodes[val]
            else:
                res = TreeNode(val)
                nodes[val] = res
            return res
        
        nodes = {}
        children = set()
        for [parent, child, is_left] in descriptions:
            parent_node = get_node(parent)
            children.add(child)
            if is_left:
                parent_node.left = get_node(child)
            else:
                parent_node.right = get_node(child)

        for node in nodes.values():
            if node.val not in children:
                return node
