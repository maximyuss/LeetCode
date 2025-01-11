// https://leetcode.com/problems/construct-k-palindrome-strings/
class Solution {
public:
    bool canConstruct(string s, int k) {
        if (s.size() < k)
            return false;
        size_t freq[26] = {0}, cntOdd = 0;
        for (char& ch : s)
            freq[ch - 'a']++;
        for (size_t ele : freq)
            cntOdd += ele & 1;
        return cntOdd <= k;
    }
};
