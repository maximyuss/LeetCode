//https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
class Solution {
public:
    bool checkTime(const vector<int>& dist, double hour, size_t time) {
        size_t n = dist.size();
        double count = 0, tmp;
        for (size_t i = 0; i < n - 1; i++) {
            tmp = ceil(dist[i] * 1.0 / time);
            count += tmp;
            if (count > hour) return false;
        }
        count += dist[n - 1] * 1.0 / time;
        return (count <= hour);
    }

    int minSpeedOnTime(vector<int>& dist, double hour) {
        size_t n = dist.size();
        if (n - 1 >= hour) return -1;
        // find the possible range
        double dl = 0, dr = 0;
        for (int e : dist) {
            dl += (e * 1.0 / hour);
            dr += (e * 1.0 / (hour - n + 1));
        }

        size_t m, l = floor(min(dl, 10e7)),
            r = ceil(min(dr, 10e7));
        while (l < r) {
            m = l + (r - l) / 2;
            if (checkTime(dist, hour, m))
                r = m;
            else
                l = m + 1;
        }
        return l;
    }
};
