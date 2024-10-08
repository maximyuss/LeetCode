// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
class Solution {
public:
    int minInsertions(string s) {
        int n = s.size(), res = 0, leftCount = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(')
                leftCount++;
            else {
                if (i + 1 == n || s[i + 1] != ')')
                    res++;
                else
                    i++;
                if (leftCount == 0)
                    res++;
                else
                    leftCount--;
            }
        }
        return res + 2 * leftCount;
    }
};
