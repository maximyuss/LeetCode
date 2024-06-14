//https://leetcode.com/problems/valid-sudoku/
class Solution {
public:
    bool check(vector<vector<char>>& board, size_t row, size_t col, char c) {
        for (size_t i = 0; i < 9; i++) {
            if (board[row][i] == c) return false;
            if (board[i][col] == c) return false;
            if (board[(row / 3) * 3 + i / 3][(col / 3) * 3 + i % 3] == c) return false;
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        char cur;
        for (size_t i = 0; i < 9; i++) {
            for (size_t j = 0; j < 9; j++) {
                cur = board[i][j];
                if (cur != '.') {
                    board[i][j] = '.';
                    if (!check(board, i, j, cur)) return false;
                    board[i][j] = cur;
                }
            }
        }
        return true;
    }
};
