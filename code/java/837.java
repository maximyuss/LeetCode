// https://leetcode.com/problems/new-21-game/
class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if (k == 0 || k - 1 + maxPts <= n) return 1.0;
        if (n < k) return 0.0;

        int right0 = Math.min(n, k + maxPts - 1);
        double window = (double)(right0 - k + 1);

        double[] dp = new double[k];
        for (int i = k - 1; i >= 0; i--) {
            double v = window / maxPts;
            dp[i] = v;
            window += v;
            int j = i + maxPts;
            if (j <= n)
                window -= (j >= k ? 1.0 : dp[j]);
        }
        return dp[0];
    }
}
