# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(row, col):
            while cols_rows[row]:
                c = cols_rows[row].pop(-1)
                while rows_cols[c]:
                    r = rows_cols[c].pop(-1)
                    dfs(r, c)

        rows_cols = defaultdict(list)
        cols_rows = defaultdict(list)
        for (r, c) in stones:
            rows_cols[c].append(r)
            cols_rows[r].append(c)
        areas = 0
        for (r, c) in stones:
            if r in rows_cols[c] and c in cols_rows[r]:
                areas += 1
                dfs(r, c)
        return len(stones) - areas
