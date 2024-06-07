class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        const size_t n = s.size();
        size_t l = 0, r;
        size_t res = 0, tmp;
        vector<size_t> pref(n + 1, 0);
        
        auto rbinSearch{ [&](size_t start) {
            size_t l = start, r = n, m;
            int cur = pref[l];
            while (l < r) {
                m = (l + r + 1) / 2;
                if ((pref[m] - cur) <= maxCost)
                    l = m;
                else
                    r = m - 1;
            }
            return l - start;
            }
        };

        for (size_t i = 0; i < n; i++) {
            if (s[i] > t[i])
                tmp = s[i] - t[i];
            else
                tmp = t[i] - s[i];
            pref[i + 1] = pref[i] + tmp;
        }
        for (size_t i = 0; i < n; i++) {
            tmp = rbinSearch(i);
            res = max(res, tmp);
        }
        return res;
    }
};
