//https://leetcode.com/problems/subsets/
class Solution {
public:
    void calcSubset(vector<int>& nums, vector<vector<int> >& res, vector<int>& subset, int index) {
        res.push_back(subset);
        for (size_t i = index; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            calcSubset(nums, res, subset, i + 1);
            subset.pop_back();
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> subset;
        vector<vector<int>> res;
        int index = 0;
        calcSubset(nums, res, subset, index);
        return res;
    }
};
