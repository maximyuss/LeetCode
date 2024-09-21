# https://leetcode.com/problems/lexicographical-numbers/
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        num = 1
        for _ in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return res
