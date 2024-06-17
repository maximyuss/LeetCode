//https://leetcode.com/problems/sqrtx/
class Solution {
public:
    int mySqrt(int num) {
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
};
