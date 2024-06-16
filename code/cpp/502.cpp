//https://leetcode.com/problems/ipo/
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        size_t n = profits.size(), idx = 0;
        vector < pair<int, int>> projects;
        priority_queue<int> pq;
        for (size_t i = 0; i < n; i++)
            projects.emplace_back(capital[i], profits[i]);
        sort(projects.begin(), projects.end());
        while (k > 0) {
            while (idx < n and projects[idx].first <= w) {
                pq.push(projects[idx].second);
                idx++;
            }
            if (pq.empty()) break;
            w += pq.top();
            pq.pop();
            k--;
        }
        return w;
    }
};
