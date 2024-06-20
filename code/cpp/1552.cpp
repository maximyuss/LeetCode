//https://leetcode.com/problems/magnetic-force-between-two-balls/
class Solution {
public:
    Solution() {ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);}
    bool checkStep(const vector<int>& pos, int m, int step) {
        size_t count = 1, idx = pos[0];
        for (size_t i = 1; i < pos.size(); i++) {
            if (pos[i] - idx >= step) {
                count++;
                idx = pos[i];
            }
            if (count == m) return true;
        }
        return false;
    }

    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        size_t res = 1, mid, l = 1, r = (position.back() - position[0]) / (m - 1);
        while (l < r) {
            mid = l + 1 + (r - l) / 2;
            if (checkStep(position, m, mid))
                l = mid;
            else
                r = mid - 1;
        }
        return l;
    }
};
