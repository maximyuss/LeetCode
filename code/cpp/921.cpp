// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution {
public:
    int minAddToMakeValid(string s) {
        size_t count_open = 0, unbalanced = 0;
        for (char ch : s) {
            if (ch == '(')
                count_open++;
            else
                count_open--;
            if (count_open == -1) {
                unbalanced++;
                count_open = 0;
            }
        }
        return unbalanced + count_open;
    }
};
