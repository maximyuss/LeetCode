//https://leetcode.com/problems/number-of-zero-filled-subarrays/
class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        size_t res = 0, n = 0;
        for (size_t i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) n++;
            else {
                res += ((n * (n + 1)) / 2);
                n = 0;
            }
        }
        res += ((n * (n + 1)) / 2);
        return res;
    }
};
