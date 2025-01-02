// https://leetcode.com/problems/count-vowel-strings-in-ranges/
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        size_t n = words.size(), m = queries.size();
        vector<int> pref(n + 1, 0), res(m);
        unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};
        for (size_t i = 0; i < n; i++) {
            pref[i + 1] = pref[i];
            if (vowels.count(words[i].front()) && vowels.count(words[i].back()))
                pref[i + 1]++;
        }
        for (size_t i = 0; i < m; i++)
            res[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
        return res;
    }
};
