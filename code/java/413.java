// https://leetcode.com/problems/arithmetic-slices/
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3)
            return 0;
        int cnt = 0, res = 0, diff = nums[1] - nums[0];
        for (int i = 1; i != nums.length - 1; i++) {
            if (nums[i + 1] - nums[i] == diff) {
                if (++cnt > 0)
                    res += cnt;
            } else {
                diff = nums[i + 1] - nums[i];
                cnt = 0;
            }
        }
        return res;
    }
}
