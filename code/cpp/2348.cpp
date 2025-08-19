//https://leetcode.com/problems/number-of-zero-filled-subarrays/
class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long res = 0;
        int cnt = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                cnt++;
                res += cnt;
            } else
                cnt = 0;
        }
        return res;
    }
};
