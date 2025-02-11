# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        res, end_char = "", part[-1]
        for c in s:
            res += c
            if c == end_char and len(res) >= n and res[-n:] == part:
                res = res[:-n]
        return res
