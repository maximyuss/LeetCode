//https://leetcode.com/problems/sum-of-all-subset-xor-totals/
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        size_t n = nums.size(),
            resXor = 0,
            resSum = 0;
        for (size_t i = 0; i < (1 << n); i++) {
            resXor = 0;
            for (size_t j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    resXor ^= nums[j];
                }
            }
            resSum += resXor;
        }
        return resSum;
    }
};
