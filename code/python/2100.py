# https://leetcode.com/problems/find-good-days-to-rob-the-bank/
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if n < (time * 2) + 1: return []
        if not time or len(set(security)) == 1: return [x for x in range(time, n - time)]
        inc_suff = [False] * n
        cnt = 0
        for i in range(n - 2, -1, -1):
            if security[i] > security[i + 1]:
                cnt = 0
            else:
                cnt += 1
                if cnt >= time: inc_suff[i] = True
        res = []
        cnt = 0
        for i in range(1, n - time):
            if security[i - 1] < security[i]:
                cnt = 0
            else:
                cnt += 1
                if cnt >= time and inc_suff[i]: res.append(i)
        return res
