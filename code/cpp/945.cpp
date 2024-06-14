//https://leetcode.com/problems/maximum-product-after-k-increments/
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        size_t res = 0, shift = 0;
        sort(nums.begin(), nums.end());
        for (size_t i = 1; i < nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) {
                shift = nums[i - 1] - nums[i] + 1;
                nums[i] += shift;
                res += shift;
            }
        }
        return res;
    }
};
