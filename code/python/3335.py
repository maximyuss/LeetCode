# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
@cache
def add(i: int):
    if i > 25:
        return add(i - 26) + add(i - 25)
    return 1

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        res = 0
        for ch in s:
            code = ord(ch) - 97
            res += add(t + code)
        return res % MOD

  '''
      def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        res = len(s)
        idx_last = 25
        for ch in s:
            freq[ord(ch) - 97] += 1
        for _ in range(t):
            res = (res + freq[idx_last]) % MOD
            idx_next = (idx_last + 1) % 26
            freq[idx_next] = (freq[idx_next] + freq[idx_last]) % MOD
            idx_last = (idx_last + 25) % 26
        return res
  '''
