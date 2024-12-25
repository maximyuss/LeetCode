// https://leetcode.com/problems/find-largest-value-in-each-tree-row/
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        deque<TreeNode*> dq{root};
        while (dq.size()) {
            int max_ = dq.front()->val, n = dq.size();
            for (size_t i = 0; i < n; i++) {
                auto cur = dq.front(); dq.pop_front();
                max_ = max(max_, cur->val);
                if (cur->left) dq.push_back(cur->left);
                if (cur->right) dq.push_back(cur->right);
            }
            res.push_back(max_);
        }
        return res;
    }
};
