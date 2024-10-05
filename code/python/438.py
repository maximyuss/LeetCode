# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p)
        if n1 < n2:
            return []
        s_freq = [0] * 26
        p_freq = [0] * 26
        res = []
        code_a = ord("a")
        for i in range(n2):
            s_freq[ord(s[i]) - code_a] += 1
            p_freq[ord(p[i]) - code_a] += 1
        if s_freq == p_freq:
            res.append(0)
        for i in range(0, n1 - n2):
            s_freq[ord(s[i]) - code_a] -= 1
            s_freq[ord(s[i + n2]) - code_a] += 1
            if s_freq == p_freq:
                res.append(i + 1)
        return res
