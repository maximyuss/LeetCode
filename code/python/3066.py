# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def choice() -> int:
            nonlocal i, j
            if i < n and (j >= cnt or nums[i] <= buff[j]):
                res = nums[i]
                i += 1
            else:
                res = buff[j]
                j += 1
            return res

        n = len(nums)
        nums.sort()
        buff = []
        i = j = cnt = 0
        while True:
            x = choice()
            if x >= k: return cnt
            y = choice()
            buff.append(2 * x + y)
            cnt += 1
