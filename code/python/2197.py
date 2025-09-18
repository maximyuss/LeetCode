# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        gcd = math.gcd
        for a in nums:
            while a > 1 and stack:
                gcd_ = gcd(a, stack[-1])
                if gcd_ == 1:
                    break
                a *= stack.pop() // gcd_
            stack.append(a)
        return stack
