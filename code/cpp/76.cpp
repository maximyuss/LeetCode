// https://leetcode.com/problems/minimum-window-substring/
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> mp;
        int res = INT_MAX, start = 0;
        for (auto e : t)
            mp[e]++;
        int count = mp.size(), l = 0, r = 0;
        while (r < s.size()) {
            mp[s[r]]--;
            if (mp[s[r]] == 0)
                count--;
            if (count == 0) {
                while (count == 0) {
                    if (res > r - l + 1) {
                        res = r - l + 1;
                        start = l;
                    }
                    mp[s[l]]++;
                    if (mp[s[l]] > 0)
                        count++;
                    l++;
                }
            }
            r++;
        }
        if (res != INT_MAX)
            return s.substr(start, res);
        else
            return "";
    }
};
