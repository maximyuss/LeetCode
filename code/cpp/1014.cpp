// https://leetcode.com/problems/best-sightseeing-pair/
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int res = 0, pref = 0;
        for (size_t i = 0; i < values.size(); i++) {
            if (pref + values[i] - i > res)
                res = pref + values[i] - i;
            if (values[i] + i > pref)
                pref = values[i] + i;
        }
        return res;
    }
};
