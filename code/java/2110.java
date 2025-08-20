// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
class Solution {
    public long getDescentPeriods(int[] prices) {
        int n = prices.length, cnt = 0;
        long res = n;
        for (int i = 1; i != n; i++) {
            if (prices[i - 1] - prices[i] == 1) {
                cnt++;
                res += cnt;
            } else
                cnt = 0;
        }
        return res;
    }
}
