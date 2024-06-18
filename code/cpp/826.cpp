//https://leetcode.com/problems/most-profit-assigning-work/
class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        size_t res = 0, n = profit.size(), idx = 0;
        vector < pair<int, int>> diff_prof (n);
        priority_queue<int> pq;
        for (size_t i = 0; i < n; i++) {
            diff_prof[i] = { difficulty[i],profit[i] };
        }
        sort(diff_prof.begin(), diff_prof.end());
        sort(worker.begin(), worker.end());
        for (size_t i = 0; i < worker.size(); i++) {
            while (idx < n and diff_prof[idx].first <= worker[i]) {
                pq.push(diff_prof[idx].second);
                idx++;
            }
            if (!pq.empty()) res += pq.top();
        }
        return res;
    }
};
