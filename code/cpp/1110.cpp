// https://leetcode.com/problems/delete-nodes-and-return-forest/

class Solution {
public:
    void dfs(TreeNode* curr, const set<int>& st, vector<TreeNode*>& res, TreeNode* parent, bool isLeft, bool isNew = false) {
        if (!curr) return;
        if (st.contains(curr->val)) {
            if (parent) {
                if (isLeft)
                    parent->left = NULL;
                else
                    parent->right = NULL;
                isNew = true;
            }
        }
        else {
            if (isNew) {
                res.emplace_back(curr);
                isNew = false;
            }
        }
        dfs(curr->left, st, res, curr, true, isNew);
        dfs(curr->right, st, res, curr, false, isNew);
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> res;
        res.reserve(1000);
        set<int> st(to_delete.begin(), to_delete.end());
        dfs(root, st, res, NULL, true, true);
        return res;
    }
};
