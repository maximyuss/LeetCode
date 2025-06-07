# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_idx = [-1] * n
        min_ch = s[-1]
        min_idx[-1] = idx = n - 1
        for i in range(n - 2, -1, -1):
            if s[i] <= min_ch:
                min_ch = s[i]
                idx = i
            min_idx[i] = idx
        res, t = [], []
        idx, idx_pre = min_idx[0], -1
        while t or idx < n:
            if not t or (idx < n and t[-1] > s[idx]):
                res.append(s[idx])
                t += [c for c in s[idx_pre + 1 : idx]]
                idx_pre = idx
                idx = min_idx[idx + 1] if idx + 1 < n else n
            else:
                res.append(t.pop())
        res += t[::-1]
        return "".join(res)
