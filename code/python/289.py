# https://leetcode.com/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def count_neibor(r, c):
            count = -(board[r][c] % 2)
            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    count += board[i][j] % 2
            return count

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                board[r][c] += count_neibor(r, c) << 1
        for r in range(rows):
            for c in range(cols):
                curr = board[r][c] % 2
                neibor = board[r][c] >> 1
                if curr == 0:
                    if neibor == 3:
                        curr = 1
                else:
                    if neibor < 2 or neibor > 3:
                        curr = 0
                board[r][c] = curr
