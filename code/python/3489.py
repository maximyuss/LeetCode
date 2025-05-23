# https://leetcode.com/problems/zero-array-transformation-iv/
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, res = len(nums), 1
        cnt_none_zero = n
        dp = [set() for _ in range(n)]
        for i, num in enumerate(nums):
            if num == 0:
                cnt_none_zero -= 1
            else:
                dp[i].add(num)
        if cnt_none_zero == 0:
            return 0
        for l, r, val in queries:
            for i in range(l, r + 1):
                if not dp[i]: continue
                new_values = []
                for num in dp[i]:
                    if num < val: continue
                    elif num == val:
                        cnt_none_zero -= 1
                        dp[i].clear()
                        break
                    else:
                        new_values.append(num - val)
                if dp[i] and new_values:
                    dp[i].update(new_values)
            if cnt_none_zero == 0:
                return res
            res += 1
        return -1
