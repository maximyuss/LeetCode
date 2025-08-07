// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/
class Solution {
    public int maxCollectedFruits(int[][] fruits) {
        int n = fruits.length;
        int x1, x2, x3;
        for (int i = 1; i < n; i++) {
            fruits[i][i] += fruits[i - 1][i - 1];

            for (int j = i + 1; j < n; j++) {
                if (i + j < n - 1) continue;
                
                x1 = (j == n - 1) ? 0 : fruits[i - 1][j + 1];
                x2 = (i + j == n - 1) ? 0 : fruits[i - 1][j];
                x3 = (j == 0 || i + j <= n) ? 0 : fruits[i - 1][j - 1];
                fruits[i][j] += max3(x1, x2, x3);

                x1 = (j == n - 1) ? 0 : fruits[j + 1][i - 1];
                x2 = (i + j == n - 1) ? 0 : fruits[j][i - 1];
                x3 = (j == 0 || i + j <= n) ? 0 : fruits[j - 1][i - 1];
                fruits[j][i] += max3(x1, x2, x3);
            }
        }

        return fruits[n - 1][n - 2] + fruits[n - 2][n - 1] + fruits[n - 1][n - 1];
    }
 
    private int max3(int a, int b, int c) {
       return Math.max(a, Math.max(b, c));
    }
}
