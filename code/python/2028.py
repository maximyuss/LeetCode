# https://leetcode.com/problems/find-missing-observations/
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        totalSum = mean * (len(rolls) + n)
        rollsSum = sum(rolls)
        missingSum = totalSum - rollsSum
        if missingSum < n or missingSum > 6 * n:
            return []
        num = missingSum // n
        reminder = missingSum % n
        res = [num] * n
        for i in range(reminder):
            res[n - i - 1] += 1
        return res
