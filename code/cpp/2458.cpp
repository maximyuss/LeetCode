//https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
class Solution {
public:
    size_t maxHeight[100001];
    size_t curMaxHeight = 0;

    void traverseLeftToRight(TreeNode* node, size_t currentHeight) {
        if (!node) return;
        maxHeight[node->val] = curMaxHeight;
        curMaxHeight = max(curMaxHeight, currentHeight);
        traverseLeftToRight(node->left, currentHeight + 1);
        traverseLeftToRight(node->right, currentHeight + 1);
    }

    void traverseRightToLeft(TreeNode* node, size_t currentHeight) {
        if (!node) return;
        maxHeight[node->val] = max(maxHeight[node->val], curMaxHeight);
        curMaxHeight = max(currentHeight, curMaxHeight);
        traverseRightToLeft(node->right, currentHeight + 1);
        traverseRightToLeft(node->left, currentHeight + 1);
    }

  vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        traverseLeftToRight(root, 0);
        curMaxHeight = 0;
        traverseRightToLeft(root, 0);
        size_t n = queries.size();
        vector<int> res(n);
        for (size_t i = 0; i < n; i++)
            res[i] = maxHeight[queries[i]];
        return res;
    }
};
