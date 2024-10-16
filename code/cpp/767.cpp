// https://leetcode.com/problems/reorganize-string/
class Solution {
public:
    string reorganizeString(string s) {
       	unordered_map<char, int> letters;
        priority_queue < pair<int, int>> pq;
        queue<pair<int, int>> q;
        for (char ch : s)
            letters[ch]++;
        for (auto it : letters)
            pq.push({ it.second, it.first });
        string res = "";
        while (pq.size()) {
            pair<int, int> cur = pq.top();
            pq.pop();
            res += cur.second;
            cur.first--;
            if (q.size()) {
                pq.push(q.front());
                q.pop();
            }
            if (cur.first != 0)
                q.push(cur);
        }
        if (q.size()) res = "";
        return res;
    }
};
