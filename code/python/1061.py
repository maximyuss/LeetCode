# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(char: str) -> int:
            idx = ord(char) - 97
            while idx != unions[idx]:
                idx = unions[idx]
            return idx

        unions = [i for i in range(26)]
        for i in range(len(s1)):
            idx1, idx2 = find(s1[i]), find(s2[i])
            if idx1 > idx2:
                unions[idx1] = idx2
            else:
                unions[idx2] = idx1
        res = ''
        for char in baseStr:
            idx = find(char)
            res += chr(idx + 97)
        return res
