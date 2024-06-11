//https://leetcode.com/problems/permutations/
class Solution {
public:
    void foo(vector<int> nums, vector<vector<int>>& res, int index) {
        if (index >= nums.size()) {
            res.push_back(nums);
            return;
        }
        for (int i = index; i < nums.size(); i++) {
            swap(nums[index], nums[i]);
            foo(nums, res, index + 1);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        foo(nums, res, 0);
        return res;
    }
};
