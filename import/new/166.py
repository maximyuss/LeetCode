# https://leetcode.com/problems/fraction-to-recurring-decimal/
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)
        whole, rem = divmod(n, d)
        if rem == 0:
            return sign + str(whole)
        pos, frac = {}, []
        while rem:
            if rem in pos:
                i = pos[rem]
                dec = "".join(frac[:i]) + "(" + "".join(frac[i:]) + ")"
                return sign + str(whole) + "." + dec
            pos[rem] = len(frac)
            rem *= 10
            digit, rem = divmod(rem, d)
            frac.append(str(digit))
        return sign + str(whole) + "." + "".join(frac)
