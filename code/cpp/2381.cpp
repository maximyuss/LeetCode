// https://leetcode.com/problems/shifting-letters-ii/
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        size_t n = s.size();
        int l, r, d;
        vector<int> change(n + 1, 0);
        for (const auto& shift : shifts) {
            l = shift[0], r = shift[1], d = shift[2];
            if (d == 0) d = -1;
            change[l] += d;
            change[r + 1] -= d;
        }
        d = 0;
        for (size_t i = 0; i < n; i++) {
            d += change[i];
            d = (d % 26 + 26) % 26;
            s[i] = 'a' + (s[i] - 'a' + d) % 26;
        }
        return s;
    }
};
