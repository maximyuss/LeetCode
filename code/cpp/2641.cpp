// https://leetcode.com/problems/cousins-in-binary-tree-ii/
class Solution {
public:
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) return root;
        queue<TreeNode*> nodes;
        nodes.push(root);
        int previousLevelSum = root->val;
        while (!nodes.empty()) {
            int levelSize = nodes.size();
            int curLevelSum = 0;
            for (int i = 0; i < levelSize; i++) {
                TreeNode* curr = nodes.front();
                nodes.pop();
                curr->val = previousLevelSum - curr->val;
                int siblingSum = 0;
                if (curr->left) siblingSum += curr->left->val;
                if (curr->right) siblingSum += curr->right->val;
                if (curr->left) {
                    curLevelSum += curr->left->val;
                    curr->left->val = siblingSum;
                    nodes.push(curr->left);
                }
                if (curr->right) {
                    curLevelSum += curr->right->val;
                    curr->right->val = siblingSum;
                    nodes.push(curr->right);
                }
            }
            previousLevelSum = curLevelSum;
        }
        return root;
    }
};
