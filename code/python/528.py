# https://leetcode.com/problems/random-pick-with-weight/
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.pref = [0] * (n + 1)
        for i in range(1, n + 1):
            self.pref[i]=self.pref[i-1] + w[i - 1]

    def pickIndex(self) -> int:
        x = random.randint(1, self.pref[-1])
        l, r = 1, len(self.pref) - 1
        while l < r:
            m = (l + r) // 2
            if self.pref[m] < x:
                l = m + 1
            else:
                r = m
        return l - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
