//https://leetcode.com/problems/time-based-key-value-store/
class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> mp;
public:
    TimeMap() {
    }

    void set(string key, string value, int timestamp) {
        mp[key].push_back({ timestamp, value });
    }

    string get(string key, int timestamp) {
        string res = "";
        if (mp.contains(key)) {
            const vector <pair<int, string>>& data = mp[key];
            if (data[0].first <= timestamp) {
                size_t l = 0, r = data.size() - 1, m;
                while (l < r) {
                    m = (l + r + 1) / 2;
                    if (data[m].first > timestamp)
                        r = m - 1;
                    else
                        l = m;
                }
                res = data[l].second;
            }
        }
        return res;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
