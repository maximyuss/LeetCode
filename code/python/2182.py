# https://leetcode.com/problems/construct-string-with-repeat-limit/
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = ''
        dq = deque(sorted(Counter(s).items()))
        while len(dq):
            k, v = dq.pop()
            cnt = min(repeatLimit, v)
            res += k * cnt
            v -= cnt
            if v:
                if len(dq):
                    k1, v1 = dq.pop()
                    res += k1
                    v1 -= 1
                    if v1:
                        dq.append((k1, v1))
                    dq.append((k, v))
        return res
