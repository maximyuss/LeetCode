// https://leetcode.com/problems/number-of-ways-to-split-array/
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        size_t n = nums.size(), res = 0;
        long long sum = 0, acc = 0;
        for (int num: nums) 
            sum += num;
        for (int i = 0; i < n - 1; i++) {
            acc += nums[i];
            res += (2 * acc >= sum);
        }
        return res;
    }
};
