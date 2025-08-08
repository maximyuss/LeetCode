# https://leetcode.com/problems/soup-servings/
class Solution:
    def soupServings(self, n: int) -> float:
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1.0
            if b <= 0: return 0.0

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            
        # For n > 4450, the answer 1.0 has an error of less than 1e-5
        if n > 4450: return 1.0
        n = (n + 24) // 25
        return dp(n, n)
