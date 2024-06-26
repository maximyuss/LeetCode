// https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
        TreeNode* res = new TreeNode(val), * curr = root, * prev = nullptr;
        if (!root) return res;
        while (curr) {
            prev = curr;
            if (curr->val > val)
                curr = curr->left;
            else
                curr = curr->right;
        }
        if (val < prev->val)
            prev->left = res;
        else
            prev->right = res;
        return root;
    }
};
