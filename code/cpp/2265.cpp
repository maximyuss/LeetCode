//https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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
    int res = 0;
    struct avg { int sum; int count; };

    avg foo(TreeNode* root) {
        if (!root) return { 0, 0 };
        avg r = foo(root->right),
            l = foo(root->left);
        int _sum = r.sum + l.sum + root->val,
            _count = r.count + l.count + 1;
        if (root->val == _sum / _count)
            res++;
        return {_sum, _count};
    }

    int averageOfSubtree(TreeNode* root) {
        foo(root);
        return res;
    }
};
