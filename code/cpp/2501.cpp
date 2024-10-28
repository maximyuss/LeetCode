// https://leetcode.com/problems/longest-square-streak-in-an-array/
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        const size_t maxValue = 100001;
        bool flag[maxValue](false);
        for (int num : nums) flag[num] = true;
        int res = -1;
        for (size_t i = 0; i < 317; i++) {
            if (!flag[i]) continue;
            size_t idx = i;
            int count = 1;
            while ((idx = idx * idx) < maxValue and flag[idx]) {
                count++;
            }
            if (count > 1) res = max(res, count);
        }
        return res;
    }
};
