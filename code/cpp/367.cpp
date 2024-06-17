//https://leetcode.com/problems/valid-perfect-square/
class Solution {
public:
    bool isPerfectSquare(int num) {
        size_t l = 0, r = num, m;
        while (l < r) {
            m = (l + r) / 2;
            if (m * m >= num)
                r = m;
            else
                l = m + 1;
        }
        return (l * l == num);
    }
};
