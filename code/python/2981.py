# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution:
    def maximumLength(self, s: str) -> int:
        s += '_'
        m = [[0, 0, 0] for i in range(26)]
        size, res = 1, 0
        l = ord(s[0]) - ord('a')
        for i in range(1, len(s)):
            r = ord(s[i]) - ord('a')
            if r == l:
                size += 1
                continue
            if size > m[l][0]:
                m[l][0] = size
                if m[l][0] > m[l][1]: m[l][0], m[l][1] = m[l][1], m[l][0]
                if m[l][1] > m[l][2]: m[l][1], m[l][2] = m[l][2], m[l][1]
                if m[l][0] > m[l][1]: m[l][0], m[l][1] = m[l][1], m[l][0]
            if size > 2:
                res = max(res, size - 2)
            if m[l][0] > 0:
                res = max(res, m[l][0])
            if m[l][1] > 0:
                if m[l][1] == m[l][2]:
                    res = max(res, m[l][2] - 1)
                else:
                    res = max(res, m[l][1])
            size = 1
            l = r
        return res if res > 0 else -1
