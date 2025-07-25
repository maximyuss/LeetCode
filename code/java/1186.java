// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
class Solution {
    public int maximumSum(int[] arr) {
        int n = arr.length;
        int[] suf = new int[n];
        suf[n - 1] = 0;
        int sum, pref = 0, res = Integer.MIN_VALUE;
        for (int i = n - 1; i > 0; i--) {
            sum = arr[i] + suf[i];
            if (sum > 0) suf[i - 1] = sum;
        }
        for (int i = 0; i < n; i++) {
            if (i > 0)
                pref = Math.max(0, arr[i - 1] + pref);
            sum = suf[i] + pref;
            if (sum == 0) {
                if (res < 0)
                    res = Math.max(res, arr[i]);
            } else
                res = Math.max(res, Math.max(sum, sum + arr[i]));
        }
        return res;
    }
}
