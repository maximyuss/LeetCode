// https://leetcode.com/problems/maximum-subarray/
class Solution {
    public int maxSubArray(int[] nums) {
        int cur_sum = 0, max_sum = nums[0];
        for (int num : nums) {
            cur_sum += num;
            if (cur_sum > max_sum) max_sum = cur_sum;
            if (cur_sum < 0) cur_sum = 0;
        }
        return max_sum;
    }
}
