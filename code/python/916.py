# https://leetcode.com/problems/word-subsets/description/
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = set(words1)
        letters = {}
        for word in words2:
            for ch in word:
                cnt = word.count(ch)
                if ch not in letters or cnt > letters[ch]:
                    letters[ch] = cnt
        for word in words1:
            for ch in letters:
                if word.count(ch) < letters[ch]:
                    res.remove(word)
                    break
        return list(res)
