# https://leetcode.com/problems/put-marbles-in-bags/
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n: return 0
        pair_weights = [0] * (n - 1)
        for i in range(n - 1):
            pair_weights[i] = weights[i] + weights[i + 1]
        pair_weights.sort()
        return sum(pair_weights[-k + 1 :]) - sum(pair_weights[: k - 1])
