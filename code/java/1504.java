// https://leetcode.com/problems/count-submatrices-with-all-ones/
class Solution {
    public int numSubmat(int[][] mat) {
        int n = mat.length, m = mat[0].length, res = 0;
        int[] height = new int[m], stack = new int[m], sum = new int[m];
        for (int i = 0; i != n; i++) {
            for (int j = 0; j != m; j++)
                height[j] = mat[i][j] == 0 ? 0 : height[j] + 1;
            int top = -1;
            for (int j = 0; j < m; j++) {
                int hj = height[j];
                while (top >= 0 && height[stack[top]] >= hj)
                    top--;
                if (top == -1)
                    sum[j] = hj * (j + 1);
                else
                    sum[j] = sum[stack[top]] + hj * (j - stack[top]);
                res += sum[j];
                stack[++top] = j;
            }
        }
        return res;
    }
}
