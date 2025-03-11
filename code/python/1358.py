# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_idx = [-1] * 3
        res = 0
        for i in range(len(s)):
            last_idx[ord(s[i]) - ord('a')] = i
            res += 1 + min(last_idx)
        return res
