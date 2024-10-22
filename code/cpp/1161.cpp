// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        queue<TreeNode*> nodes;
        nodes.push(root);
        int res = 1, level = 1;
        long long level_max = root->val;
        while (!nodes.empty()) {
            size_t n = nodes.size();
            long long level_sum = 0;
            while (n--) {
                auto node = nodes.front();
                nodes.pop();
                level_sum += node->val;
                if (node->left)
                    nodes.push(node->left);
                if (node->right)
                    nodes.push(node->right);
            }
            if (level_sum > level_max) {
                level_max = level_sum;
                res = level;
            }
            level++;
        }
        return res;
    }
};
