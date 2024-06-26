// https://leetcode.com/problems/balance-a-binary-search-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> arr{};

    void inorderTraversal(TreeNode* root) {
        if (!root) return;
        inorderTraversal(root->left);
        arr.emplace_back(root->val);
        inorderTraversal(root->right);
    }

    TreeNode* sortedArrayToBST(int l, int r) {
        if (r < l) return NULL;
        int mid = l + (r - l) / 2;
        TreeNode* node = new TreeNode((arr[mid]));
        node->left = sortedArrayToBST(l, mid - 1);
        node->right = sortedArrayToBST(mid + 1, r);
        return node;
    }

    TreeNode* balanceBST(TreeNode* root) {
        inorderTraversal(root);
        return sortedArrayToBST(0, arr.size() - 1);
    }
};
