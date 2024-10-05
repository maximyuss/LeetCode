# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        code_a = ord("a")
        for i in range(n1):
            s1_freq[ord(s1[i]) - code_a] += 1
            s2_freq[ord(s2[i]) - code_a] += 1
        if s1_freq == s2_freq:
            return True
        for i in range(n1, n2):
            s2_freq[ord(s2[i - n1]) - code_a] -= 1
            s2_freq[ord(s2[i]) - code_a] += 1
            if s1_freq == s2_freq:
                return True
        return False
