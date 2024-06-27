// https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution {
public:
    vector<int> res;
    int maxGroup = 0, currGroup = 0, currVal = 0;

    void dfs(TreeNode* root) {
        if (!root)
            return;
        dfs(root->left);

        if (root->val == currVal)
            currGroup++;
        else {
            currGroup = 1;
            currVal = root->val;
        }
        if (currGroup > maxGroup) {
            res = {};
            maxGroup = currGroup;
        }
        if (currGroup == maxGroup)
            res.emplace_back(root->val);

        dfs(root->right);
    }

    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return res;
    }
};
