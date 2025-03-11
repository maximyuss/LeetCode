# https://leetcode.com/problems/vowels-of-all-substrings/
class Solution:
    def countVowels(self, word: str) -> int:
        n, res = len(word), 0
        for i in range(n):
            if word[i] in {'a', 'e', 'i', 'o', 'u'}:
                res += (n - i) * (i + 1)
        return res
