// https://leetcode.com/problems/minimum-time-difference/
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        size_t i = 0, n = timePoints.size(), tmp;
        int res;
        vector<int> timeInt(n);
        for (const string& s : timePoints) {
            tmp = ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + (s[4] - '0');
            timeInt[i] = tmp;
            i++;
        }
        sort(timeInt.begin(), timeInt.end());
        res = 24 * 60 - timeInt[n - 1] + timeInt[0];
        for (int i = 1; i < n; i++)
            res = min(res, timeInt[i] - timeInt[i - 1]);
        return res;
    }
};
