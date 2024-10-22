// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        queue<TreeNode*> level;
        vector<long long> res;
        level.push(root);
        while (!level.empty()) {
            size_t n = level.size();
            long long level_sum = 0;
            while (n--) {
                auto node = level.front();
                level.pop();
                level_sum += node->val;
                if (node->left)
                    level.push(node->left);
                if (node->right)
                    level.push(node->right);
            }
            res.push_back(level_sum);
        }
        if (res.size() < k)
            return -1;
        sort(res.begin(), res.end(), greater<long long>());
        return res[k - 1];
    }
};
