# https://leetcode.com/problems/sort-vowels-in-a-string
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        counts = Counter(s)
        for v in vowels:
            s = s.replace(v, '_')
        for v in vowels:
            cnt = counts.get(v, 0)
            if cnt:
                s = s.replace('_', v, cnt)
        return s
