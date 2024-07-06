// https://leetcode.com/problems/valid-triangle-number/

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        size_t count = 0, n = nums.size(), l, r;
        for (size_t i = n - 1; i > 0; i--) {
            int c = nums[i];
            l = 0;
            r = i - 1;
            while (l < r) {
                if (nums[l] + nums[r] > c) {
                    count += r - l;
                    r--;
                } else
                    l++;
            }
        }
        return count;
    }
};
