# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        def traverse(level, idx):
            if idx == m: return 1
            if level == n: return 0
            if dp[level][idx] != -1: return dp[level][idx]
            ways = traverse(level + 1, idx)
            if target[idx] in freq[level]:
                count = freq[level][target[idx]]
                ways = (ways + count * traverse(level + 1, idx + 1)) % mod
            dp[level][idx] = ways
            return ways

        mod = 10**9 + 7
        n = len(words[0])
        m = len(target)
        freq = [{} for _ in range(n)]
        for word in words:
            for i in range(n):
                freq[i][word[i]] = freq[i].get(word[i], 0) + 1
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return traverse(0, 0)
