//https://leetcode.com/problems/sum-of-square-numbers/description/
class Solution {
public:
    inline int mySqrt(int num) {
        size_t l = 0, r = num, m;
        while (l < r) {
            m = (l + r + 1) / 2;
            if (m * m <= num)
                l = m;
            else
                r = m - 1;
        }
        return l;
    }

    bool judgeSquareSum(int c) {
        size_t l = 0, r = mySqrt(c), f;
        while (l <= r) {
            f = l * l + r * r;
            if (f >= c) {
                if (f == c) return true;
                r--;
            }
            else
                l++;
        }
        return false;
    }
};
