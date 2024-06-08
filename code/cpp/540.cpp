//https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        size_t n = nums.size() - 1;
        if (n == 0) return nums[0];
        size_t l = 0, r = n, m;
        while (l < r) {
            if (nums[l] != nums[l + 1]) return nums[l];
            if (nums[r] != nums[r - 1]) return nums[r];
            m = (l + r) / 2;
            m += (1 - m % 2);
            if (nums[m] != nums[m - 1] and nums[m] != nums[m + 1]) return nums[m];
            if (nums[m] == nums[m - 1]) 
                l = m + 1;
            if (nums[m] == nums[m + 1])
                r = m - 1;
        }
        return nums[l];
    }
};
