// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<pair<int, int>> merged;
        int n = nums.size();
        for (int i = 0; i < n; i++)
            for (int num : nums[i])
                merged.push_back({num, i});
        sort(merged.begin(), merged.end());
        unordered_map<int, int> freq;
        vector<int> res{0, 100001};
        int l = 0, count = 0;
        for (int r = 0; r < merged.size(); r++) {
            auto [num, idx] = merged[r];
            freq[idx]++;
            count += (freq[idx] == 1);
            while (count == n) {
                int cur_range = num - merged[l].first;
                if (cur_range < res[1] - res[0]) {
                    res[0] = merged[l].first;
                    res[1] = num;
                }
                freq[merged[l].second]--;
                if (not freq[merged[l].second])
                    count--;
                l++;
            }
        }
        return res;
    }
};
