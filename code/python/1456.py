# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        res = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)
        return res
