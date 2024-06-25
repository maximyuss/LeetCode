# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map<int, vector<int>> mp;
        vector<vector<int>> res;
        for (size_t i = 0; i < groupSizes.size(); i++) {
            if (groupSizes[i] == 1) {
                res.emplace_back();
                res.back().emplace_back(i);
            }
            else
                mp[groupSizes[i]].emplace_back(i);
        }
        for (auto e : mp) {
            for (size_t i = 0; i < e.second.size(); i++){
                if (i % e.first == 0)
                    res.emplace_back();
                res.back().emplace_back(e.second[i]);
            }
        }
        return res;
    }
};
