// https://leetcode.com/problems/create-binary-tree-from-descriptions/

class Solution {
public:
    TreeNode* getNode(auto& nodes, int val) {
        TreeNode* res;
        if (nodes.contains(val))
            res = nodes[val];
        else {
            res = new TreeNode(val);
            nodes[val] = res;
        }
        return res;
    }

    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        unordered_set<int> children;

        for (const auto& description : descriptions) {
            int parent = description[0], 
                child = description[1];
            bool isLeft = description[2];
            TreeNode* parent_node = getNode(nodes, parent);
            children.insert(child);
            if (isLeft)
                parent_node->left = getNode(nodes, child);
            else
                parent_node->right = getNode(nodes, child);
        }
        for (auto& node : nodes)
            if (!children.contains(node.first))
                return node.second;
        return nullptr;
    }
};
