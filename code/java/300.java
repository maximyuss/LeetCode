// https://leetcode.com/problems/longest-increasing-subsequence/
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] res = new int[nums.length];
        int n = 0;
        for (int num: nums) {
            int l = 0, r = n, m;
            while (l < r) {
                m = l + (r - l) / 2;
                if (res[m] < num)
                    l = m + 1;
                else
                    r = m;
            }
            res[l] = num;
            if (l == n)
                n++;
        }
        return n;
    }
}
