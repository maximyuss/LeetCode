// https://leetcode.com/problems/largest-merge-of-two-strings/
class Solution {
public:
    string largestMerge(string word1, string word2) {
        size_t i1 = 0, i2 = 0, n1 = word1.size(), n2 = word2.size();
        string res;
        while (i1 < n1 and i2 < n2) {
            if (word1[i1] > word2[i2])
                res += word1[i1++];
            else if (word1[i1] < word2[i2])
                res += word2[i2++];
            else {
                size_t j1 = i1 + 1, j2 = i2 + 1;
                while (j1 < n1 and j2 < n2 and word1[j1] == word2[j2])
                    j1++, j2++;
                if (word1[j1] > word2[j2] or (word1[j1] == word2[j2] and n1 - j1 > n2 - j2))
                    res += word1[i1++];
                else
                    res += word2[i2++];
            }
        }
        if (i1 < n1) res += word1.substr(i1);
        if (i2 < n2) res += word2.substr(i2);
        return res;
    }
};
