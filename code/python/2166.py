# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1: return False
        p_open, p_any = [], []
        for i in range(n):
            if locked[i] == "0":
                p_any.append(i)
            elif s[i] == "(":
                p_open.append(i)
            else:
                if p_open:
                    p_open.pop()
                elif p_any:
                    p_any.pop()
                else:
                    return False
        while p_open and p_any and p_open[-1] < p_any[-1]:
            p_open.pop()
            p_any.pop()
        if p_open: return False
        return True
