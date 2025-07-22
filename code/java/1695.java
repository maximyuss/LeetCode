// https://leetcode.com/problems/maximum-erasure-value/
class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int n = nums.length, max = 0, left = 0;
        for (int num : nums) if (num > max) max = num;
        boolean[] inWindow = new boolean[max + 1];
        long sum = 0, res = 0;
        for (int right = 0; right < n; right++) {
            int num = nums[right];
            while (inWindow[num]) {
                inWindow[nums[left]] = false;
                sum -= nums[left];
                left++;
            }
            inWindow[num] = true;
            sum += num;
            if (sum > res) res = sum;
        }
        return (int) res;
    }
}
