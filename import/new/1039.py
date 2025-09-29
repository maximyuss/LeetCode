# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                vi = values[i]
                vj = values[j]
                vij = vi * vj
                row_i = dp[i]
                best = 1 << 62
                for k in range(i + 1, j):
                    s = row_i[k] + dp[k][j] + vij * values[k]
                    if s < best:
                        best = s
                row_i[j] = best
        return dp[0][n - 1]
