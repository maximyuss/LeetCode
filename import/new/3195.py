# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i
class Solution {
    public int minimumArea(int[][] grid) {
        int n = grid.length, m = grid[0].length;    
        int y0 = 0;
        for (; y0 < n; y0++) {
            int[] r = grid[y0];
            int j = 0; for (; j < m && r[j] == 0; j++);
            if (j < m) break;
        }
        if (y0 == n) return 0;
        int y1 = n - 1;
        for (;; y1--) {
            int[] r = grid[y1];
            int j = 0; for (; j < m && r[j] == 0; j++);
            if (j < m) break;
        }
        int x0 = 0;
        outer0:
        for (; x0 < m; x0++) {
            for (int i = y0; i <= y1; i++) 
                if (grid[i][x0] != 0) break outer0;
        }
        int x1 = m - 1;
        outer1:
        for (; x1 >= 0; x1--) {
            for (int i = y0; i <= y1; i++) 
                if (grid[i][x1] != 0) break outer1;
        }
        return (x1 - x0 + 1) * (y1 - y0 + 1);
    }
}
