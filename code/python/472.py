# https://leetcode.com/problems/concatenated-words/
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def check(word) -> bool:
            n = len(word)
            dp = [True] + [False] * n
            for i in range(0, n):
                for j in range(n, max(i - 1, i + min_len - 1), -1):
                    if i == 0 and j == n: continue
                    elem = word[i:j]
                    if dp[i] and elem in words_set:
                        if j == n: return True
                        dp[j] = True
            return False

        words_set = set(words)
        n = len(words)
        min_len = 99
        for word in words:
            tmp = len(word)
            if tmp < min_len:
                min_len = tmp
        res = []
        for word in words:
            if len(word) >= min_len * 2 and check(word):
                res.append(word)
        return res
