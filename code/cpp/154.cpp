class Solution {
public:
    int findMin(vector<int>& nums) {
        int res = nums[0], 
            n = nums.size() - 1;
        if (n == 0 or nums[0] < nums[n]) return nums[0];
        if (nums[n] < nums[n - 1]) return nums[n];
        for (size_t i = 1; i < nums.size(); i++)    {
            res = min(res, nums[i]);
        }
        return res;
    }
};
