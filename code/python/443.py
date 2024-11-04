# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        idx, n = 0, len(chars)
        while idx < n:
            first = chars[idx]
            cnt = 0
            while idx < n and chars[idx] == first:
                idx += 1
                cnt += 1
            chars[res] = first
            res += 1
            if cnt > 1:
                for ch in str(cnt):
                    chars[res] = ch
                    res += 1
        return res
