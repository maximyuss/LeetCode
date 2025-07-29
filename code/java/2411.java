// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int n = nums.length, res[] = new int[n];
        for (int i = 0; i != n; i++) {
            res[i] = 1;
            int j = i - 1;
            while (j >= 0 && (nums[j] | nums[i]) != nums[j]) {
                res[j] = i - j + 1;
                nums[j] |= nums[i];
                j--;
            }
        }
        return res;
    }
}
