//https://leetcode.com/problems/maximum-product-after-k-increments/
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        const long long modulo = 1e9 + 7;
        long long res = 1;
        int n = k;
        size_t idx = 1, shift = 0;
        if (nums.size() == 1) return nums[0] + k;
        sort(nums.begin(), nums.end());
        while (n > 0) {
            if (idx < nums.size()) {
                if (nums[idx] >= nums[0]) {
                    shift = min(nums[1] - nums[0] + 1, n);
                    nums[0] += shift;
                    n -= shift;
                    idx = 1;
                }
                if (nums[idx] < nums[0]) {
                    shift = min(nums[0] - nums[idx], n);
                    nums[idx] += shift;
                    n -= shift;
                    idx++;
                }
            }
            else idx = 1;
        }
        for (int e : nums) {
            res *= e;
            res %= modulo;
        }
        return res;
    }
};
