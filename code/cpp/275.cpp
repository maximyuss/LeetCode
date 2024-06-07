class Solution {
public:
    int hIndex(vector<int>& citations) {
        int m,
            l = 0,
            n = citations.size(),
            r = n - 1,
            res = 0;
        while (l <= r) {
            m = (l + r) / 2;
            if (citations[m] >= n - m) {
                res = max(res, n - m);
                r = m - 1; 
            } else
                l = m + 1;
        }
        return res;
    }
};
