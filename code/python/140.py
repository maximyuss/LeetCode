# https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def foo(i, candidate):
            for j in range(n, i - 1, -1):
                elem = s[i:j]
                if elem in dict_set:
                    candidate.append(elem)
                    if j == n:
                        res.append(" ".join(candidate))
                        candidate.pop()
                    else:
                        foo(j, candidate)
                        candidate.pop()

        n = len(s)
        dict_set = set(wordDict)
        res = []
        foo(0, [])
        return res
