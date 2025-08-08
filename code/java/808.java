// https://leetcode.com/problems/soup-servings/
class Solution {
    private Double[][] memo;

    public double soupServings(int n) {
        // For n > 4450, the answer 1.0 has an error of less than 1e-5
        if (n > 4450) return 1.0;
        n = (n + 24) / 25;
        memo = new Double[n + 1][n + 1];
        return dp(n, n);
    }

    private double dp(int a, int b) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;

        if (memo[a][b] != null) return memo[a][b];
        memo[a][b] = 0.25 * (dp(a - 4, b) +
            dp(a - 3, b - 1) +
            dp(a - 2, b - 2) +
            dp(a - 1, b - 3));
        return memo[a][b];
    }
}
