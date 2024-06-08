#https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lenS, lenT = len(s), len(t)
        idxS = idxT = 0
        while idxS < lenS and idxT < lenT:
            if s[idxS] == t[idxT]:
                idxT += 1
            idxS += 1
        return lenT - idxT
