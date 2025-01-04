// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int res = 0, l, r;
        for (char ch = 'a'; ch <= 'z'; ch++) {
            l = s.find(ch), r = s.rfind(ch);
            if (l + 1 > r)
                continue;
            bitset<26> seen = 0;
            for (size_t i = l + 1; i < r; i++)
                seen[s[i] - 'a'] = 1;
            res += seen.count();
        }
        return res;
    }
};
