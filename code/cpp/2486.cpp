https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
class Solution {
public:
    int appendCharacters(string s, string t) {
        size_t nS = s.size(), nT = t.size(),
            idxS = 0, idxT = 0;
        while (idxS < nS and idxT < nT) {
            if (s[idxS] == t[idxT])
                idxT++;
            idxS++;
        }
        return nT - idxT;
    }
};
