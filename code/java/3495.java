// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero
public class Solution {
    public long minOperations(int[][] queries) {
        final int MAX_I = 16;
        long[] pref = new long[MAX_I];
        for (int i = 1; i < MAX_I; i++) {
            pref[i] = ((((long)(3 * i - 1)) << (2 * i)) + 1L) / 3L;
        }

        long res = 0;
        for (int[] q : queries) {
            int l = q[0], r = q[1];

            int base_l = base(l), base_r = base(r);

            long cur_res;
            if (base_l == base_r)
                cur_res = (long)(r - l + 1) * base_l;
            else {
                cur_res = pref[base_r - 1] - pref[base_l];
                cur_res += (long)(r - ((1L << (2 * (base_r - 1))) - 1)) * base_r;
                cur_res += (long)((1L << (2 * base_l)) - l) * base_l;
            }
            res += (cur_res + 1) / 2;
        }
        return res;
    }

    private int base(int x) {
        if (x == 0) return 0;
        int bits = 32 - Integer.numberOfLeadingZeros(x);
        return (bits + 1) / 2;
    }
}
