# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)
        n = len(s)
        dp = [True] + [False] * (n)
        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub in dict_set and dp[j]:
                    dp[i] = True
        return dp[n]
