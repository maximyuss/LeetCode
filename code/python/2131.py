# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        freq = Counter(words)
        has_double = False
        for k, v in freq.items():
            if k[0] == k[1]:
                res += v // 2 * 4
                if v & 1:
                    has_double = True
            else:
                res += 4 * min(v, freq[k[1] + k[0]])
                freq[k] = 0
        return res + has_double * 2
