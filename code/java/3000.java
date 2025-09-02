// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        long max_diag_sq = 0, max_area = 0;
        for (int[] d : dimensions) {
            long cur_diag_sq = d[0]*d[0] + d[1]*d[1];
            if (cur_diag_sq > max_diag_sq) {
                max_diag_sq = cur_diag_sq;
                max_area = d[0] * d[1];
            }
            else if (cur_diag_sq == max_diag_sq)
                max_area = Math.max(max_area, d[0] * d[1]);
        }
        return (int) max_area;
    }
}
