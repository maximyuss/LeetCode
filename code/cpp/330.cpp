//https://leetcode.com/problems/patching-array/
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        size_t idx = 0, count = 0, sum = 1, numsSize = nums.size();
        while (sum <= n) {
            if (idx < numsSize and nums[idx] <= sum) {
                sum += nums[idx++];
            }
            else {
                sum += sum;
                count++;
            }
        }
        return count;
    }
};
