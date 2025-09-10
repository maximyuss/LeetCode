# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            x = num1 - num2 * i
            if x >= 0 and x.bit_count() <= i <= x:
                return i
        return -1
