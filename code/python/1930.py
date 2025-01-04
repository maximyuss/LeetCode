# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res, A = 0, ord('a')
        for ch in range(26):
            c = chr(ch + A)
            l, r = s.find(c), s.rfind(c)
            if l != r:
                res += len(set(s[l + 1:r]))
        return res
