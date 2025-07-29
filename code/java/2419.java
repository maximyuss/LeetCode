// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
class Solution {
    public int longestSubarray(int[] nums) {
        int max = nums[0], longest = 0, cur = 0;
        for (int num : nums) max = Math.max(max, num);
        for (int num : nums) {
            if (num == max)
                cur++;
            else {
                longest = Math.max(longest, cur);
                cur = 0;
            }
        }
        return Math.max(longest, cur);
    }
}
