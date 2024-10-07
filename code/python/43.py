# https://leetcode.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        n1, n2 = len(num1), len(num2)
        if n1 < n2:
            num1, num2 = num2, num1
            n1, n2 = n2, n1
        nums1 = list(map(int, num1))
        nums2 = list(map(int, num2))
        res = [0] * (n1 + n2)
        for i in range(n2 - 1, -1, -1):
            shift = 0
            for j in range(n1 - 1, -1, -1):
                c = res[i + j + 1] + nums2[i] * nums1[j] + shift
                shift = 0
                if c > 9:
                    shift = c // 10
                    c %= 10
                res[i + j + 1] = c
            else:
                res[i + j] += shift
        start = 1 if res[0] == 0 else 0
        res_str = "".join(map(str, res[start:]))
        return res_str
