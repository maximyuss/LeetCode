# https://leetcode.com/problems/minimum-penalty-for-a-shop/
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_penalty = penalty = 0
        res = -1
        for i, c in enumerate(customers):
            penalty += 1 if c == 'Y' else -1
            if penalty > max_penalty:
                max_penalty = penalty
                res = i
        return res + 1
