// https://leetcode.com/problems/frequency-of-the-most-frequent-element/
class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        long sum = k;
        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            sum += nums[r];
            if (sum < (long) nums[r] * (r - l + 1))
                sum -= nums[l++];
        }
        return nums.length - l;
    }
}
