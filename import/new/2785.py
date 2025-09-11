# https://leetcode.com/problems/sort-vowels-in-a-string
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_order = "AEIOUaeiou"
        counts = Counter(s)
        for v in vowels_order:
            s = s.replace(v, '_')
        for v in vowels_order:
            cnt = counts.get(v, 0)
            if cnt:
                s = s.replace('_', v, cnt)
        return s
