# https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            nonlocal maxGroup, currGroup, currVal, res
            if not root:
                return
            dfs(root.left)

            if root.val == currVal:
                currGroup += 1
            else:
                currGroup = 1
                currVal = root.val
            if currGroup > maxGroup:
                res = []
                maxGroup = currGroup
            if currGroup == maxGroup:
                res.append(root.val)

            dfs(root.right)

        maxGroup = currGroup = currVal = 0
        res = []
        dfs(root)
        return res
