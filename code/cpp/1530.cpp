// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution {
public:
    vector<int> dfs(TreeNode* root, int distance) {
        vector<int> countCurr(12, 0);
        if (root) {
            if (!root->left && !root->right)
                countCurr[0] = 1;
            else {
                vector<int> countLeft, countRight;
                countLeft = dfs(root->left, distance);
                countRight = dfs(root->right, distance);
                for (size_t i = 0; i < 10; i++)
                    countCurr[i + 1] = countLeft[i] + countRight[i];
                countCurr[11] += countLeft[11] + countRight[11];
                for (size_t i = 0; i <= distance; i++)
                    for (size_t j = 0; j <= distance; j++)
                        if (2 + i + j <= distance)
                            countCurr[11] += countLeft[i] * countRight[j];
            }
        }
        return countCurr;
    }

    int countPairs(TreeNode* root, int distance) {
        vector<int> res;
        res = dfs(root, distance);
        return res[11];
    }
};
