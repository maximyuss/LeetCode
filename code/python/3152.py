# https://leetcode.com/problems/special-array-ii/
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix, res = [0] * len(nums), [True] * len(queries)
        prev = nums[0] % 2
        for i in range(1, len(nums)):
            curr = nums[i] % 2
            prefix[i] = prefix[i - 1] + (1 if curr == prev else 0)
            prev = curr
        for i, query in enumerate(queries):
            if prefix[query[1]] - prefix[query[0]] > 0:
                res[i] = False
        return res
