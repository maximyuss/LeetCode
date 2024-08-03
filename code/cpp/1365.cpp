// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> dict;
        vector<int> res(n), 
            sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        for (int i = n - 1; i > -1; i--)
            dict[sorted_nums[i]] = i;
        for (int i = 0; i < n; i++)
            res[i] = dict[nums[i]];
        return res;
    }
};
