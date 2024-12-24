// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
class FindElements {
private:
	TreeNode* root;

	void recovery(int val, TreeNode* cur) {
		cur->val = val;
		if (cur->left) recovery(2 * val + 1, cur->left);
		if (cur->right) recovery(2 * val + 2, cur->right);
	}

public:
	FindElements(TreeNode* root) {
		this->root = root;
		recovery(0, root);
	}

	bool find(int target) {
		if (target == 0) return true;
		stack<int> st;
		auto cur = this->root;
		while (target) {
			st.push(target);
			target = (target - 1) / 2;
		}
		while (st.size()) {
			int node = st.top();
			st.pop();
			if (cur->left and cur->left->val == node) cur = cur->left;
			else if (cur->right and cur->right->val == node) cur = cur->right;
			else return false;
		}
		return true;
	}
};
