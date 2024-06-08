//https://leetcode.com/problems/powx-n/
class Solution {
public:
    double foo(double x, size_t n) {
        if (n == 0 or x == 1) return 1.0;
        if (n % 2) return x * foo(x, n - 1); 
        else return foo(x * x, n / 2);
    }

    double myPow(double x, int n) {
        if (n < 0) {
            long ln = n;
            ln = -ln;
            return 1 / foo(x, ln);
        }
        return foo(x, n);
    }

};
