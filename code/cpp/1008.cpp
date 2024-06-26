// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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
    int idx = 0, n;

    TreeNode* build(vector<int>& arr, int _max) {
        if (idx == n || arr[idx] > _max) return NULL;
        TreeNode* root = new TreeNode(arr[idx++]);
        root->left = build(arr, root->val);
        root->right = build(arr, _max);
        return root;
    }

    TreeNode* bstFromPreorder(vector<int>& preorder) {
        n = preorder.size();
        return build(preorder, 1001);
    }
};
