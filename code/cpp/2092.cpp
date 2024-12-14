// https://leetcode.com/problems/find-all-people-with-secret/
class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<forward_list<pair<int, int>>> graph(n);
        for (const auto& meeting : meetings) {
            graph[meeting[0]].emplace_front(meeting[2], meeting[1]);
            graph[meeting[1]].emplace_front(meeting[2], meeting[0]);
        }
        priority_queue<pair<int, int>, vector<std::pair<int, int>>, greater<std::pair<int, int>>> pq;
        vector<bool> visited(n, false);
        pq.emplace(0, 0);
        pq.emplace(0, firstPerson);
        while (!pq.empty()) {
            const auto [time, person] = pq.top();
            pq.pop();
            if (visited[person])
                continue;
            visited[person] = true;
            for (const auto& [t, next_person] : graph[person])
                if (!visited[next_person] and t >= time)
                    pq.emplace(t, next_person);
        }
        vector<int> res;
        for (size_t i = 0; i < n; i++)
            if (visited[i])
                res.emplace_back(i);
        return res;
    }
};
