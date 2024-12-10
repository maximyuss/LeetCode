# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for l in set(s):
            if s.count(l) < k:
                res = 0
                for sub_s in s.split(l):
                    res = max(res, self.longestSubstring(sub_s, k))
                return res
        return len(s)
