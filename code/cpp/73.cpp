// https://leetcode.com/problems/set-matrix-zeroes/
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();
        bool first_row_zero = false, first_col_zero = false;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == 0) {
                    if (r == 0) first_row_zero = true;
                    if (c == 0) first_col_zero = true;
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }
        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                if (matrix[0][c] == 0 or matrix[r][0] == 0)
                    matrix[r][c] = 0;
        if (first_row_zero)
            for (int c = 0; c < cols; c++)
                matrix[0][c] = 0;
        if (first_col_zero)
            for (int r = 0; r < rows; r++)
                matrix[r][0] = 0;
    }
};
