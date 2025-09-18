# https://leetcode.com/problems/number-of-stable-subsequences/
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        even1 = even2 = odd1 = odd2 = 0
        for val in nums:
            if val % 2 == 0:
                new_even1 = (even1 + odd1 + odd2 + 1) % MOD
                new_even2 = (even2 + even1) % MOD
                even1, even2 = new_even1, new_even2
            else:
                new_odd1 = (odd1 + even1 + even2 + 1) % MOD
                new_odd2 = (odd2 + odd1) % MOD
                odd1, odd2 = new_odd1, new_odd2
        return (even1 + even2 + odd1 + odd2) % MOD
