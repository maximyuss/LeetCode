// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    TreeNode* bstToGst(TreeNode* root) {
        int _sum = 0;
        foo(root, _sum);
        return root;
    }
private:
    void foo(TreeNode* root, int & _sum) {
        if (!root) return;
        foo(root->right, _sum);
        _sum += root->val;
        root->val = _sum;
        foo(root->left, _sum);
    }
};
