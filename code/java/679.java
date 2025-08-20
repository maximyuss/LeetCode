// https://leetcode.com/problems/24-game/
class Solution {
        private static final double EPS = 1e-6;

    public boolean judgePoint24(int[] nums) {
        double[] A = new double[nums.length];
        for (int i = 0; i < nums.length; i++) A[i] = nums[i];
        return dfs(A, A.length);
    }

    private boolean dfs(double[] A, int n) {
        if (n == 1) return Math.abs(A[0] - 24.0) < EPS;
        int m = n - 1;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                double a = A[i], b = A[j];
                A[j] = A[m];
                A[i] = a + b;
                if (dfs(A, m)) return true;
                A[i] = a * b;
                if (dfs(A, m)) return true;
                A[i] = a - b;
                if (dfs(A, m)) return true;
                if (Math.abs(a - b) > EPS) {
                    A[i] = b - a;
                    if (dfs(A, m)) return true;
                }
                if (Math.abs(b) > EPS) {
                    A[i] = a / b;
                    if (dfs(A, m)) return true;
                }
                if (Math.abs(a) > EPS && Math.abs(a - b) > EPS) {
                    A[i] = b / a;
                    if (dfs(A, m)) return true;
                }
                A[i] = a;
                A[j] = b;
            }
        }
        return false;
    }
}
