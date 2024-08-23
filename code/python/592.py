# https://leetcode.com/problems/fraction-addition-and-subtraction/
class Solution:
    def fractionAddition(self, expression: str) -> str:
        parts = re.findall(r'[+-]?\d+', expression)
        res_num = 0
        res_den = 1
        for i in range(0, len(parts), 2):
            # Reading numbers
            cur_num = int(parts[i])
            cur_den = int(parts[i + 1])
            # Evaluating an expression
            if res_den == cur_den:
                res_num += cur_num
            else:
                res_num = res_num * cur_den + cur_num * res_den
                res_den *= cur_den
            # Normalization of a fraction
            gcd = math.gcd(res_num, res_den)
            if gcd != 1:
                res_num //= gcd
                res_den //= gcd
        return str(res_num) + "/" + str(res_den)
