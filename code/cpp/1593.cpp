//https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
class Solution {
public:
    unordered_set<string> seen;
    void backtrack(const string& s, const size_t start, size_t& res) {
        size_t count = seen.size(), n = s.size();
        if (count + n - start <= res) return;
        if (start == n) {
            res = max(res, count);
            return;
        }
        for (size_t i = start + 1; i <= n; i++) {
            string subStr = s.substr(start, i-start);
            if (!seen.contains(subStr)) {
                seen.insert(subStr);
                backtrack(s, i, res);
                seen.erase(subStr);
            }
        }
    }

    int maxUniqueSplit(string s) {
        size_t res = 0;
        backtrack(s, 0, res);
        return res;
    }
};
