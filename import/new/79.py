# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n: return False

        bc = Counter(ch for row in board for ch in row)
        wc = Counter(word)
        for ch, need in wc.items():
            if need > bc.get(ch, 0): return False
        if bc[word[0]] > bc[word[-1]]:
            word = word[::-1]

        def dfs(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
                return False
            cur = board[i][j]
            board[i][j] = '#'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(i + dx, j + dy, k + 1):
                    return True
            board[i][j] = cur
            return False

        start = word[0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == start and dfs(i, j, 0):
                    return True
        return False
