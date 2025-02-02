# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = cnt_b = 0
        for ch in s:
            if ch == "b":
                cnt_b += 1
            elif cnt_b:
                res += 1
                cnt_b -= 1
        return res
