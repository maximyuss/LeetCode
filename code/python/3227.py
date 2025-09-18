// https://leetcode.com/problems/vowels-game-in-a-string/
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
