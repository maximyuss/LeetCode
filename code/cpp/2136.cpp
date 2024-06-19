//https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        size_t n = plantTime.size(), totalPlantTime = -1, totalMaxTime = 0;
        vector <pair<int, size_t>> pairs (n);
        for (size_t i = 0; i < n; i++) {
            pairs[i] = { growTime[i], plantTime[i] };
        }
        sort(pairs.begin(), pairs.end());
        for (size_t i = n - 1; i + 1 != 0; i--) {
            totalPlantTime += pairs[i].second;
            totalMaxTime = max(totalMaxTime, totalPlantTime + pairs[i].first);
        }
        return totalMaxTime + 1;
    }
};
