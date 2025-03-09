# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        res = total = sum(cardPoints[:k])
        for i in range(1, k + 1):
            total += -cardPoints[k - i] + cardPoints[n - i]
            res = max(res, total)
        return res
