# https://leetcode.com/problems/construct-k-palindrome-strings/
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n == k: return True
        if n < k: return False
        dict = Counter(s)
        count_odd = sum(x & 1 for x in dict.values())
        return count_odd <= k
