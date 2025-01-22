// https://leetcode.com/problems/map-of-highest-peak/
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        size_t m = isWater.size(), n = isWater[0].size();
        deque<pair<int, int>> dq;
        vector<vector<int>> heights(m, vector<int>(n, -1));
        int shifts[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (size_t i = 0; i != m; i++)
            for (size_t j = 0; j != n; j++)
                if (isWater[i][j] == 1) {
                    dq.push_back({i, j});
                    heights[i][j] = 0;
                }
        size_t x, y, h, nx, ny;
        while (dq.size()) {
            x = dq.front().first, y = dq.front().second, h = heights[x][y];
            dq.pop_front();
            for (size_t i = 0; i != 4; i++) {
                nx = x + shifts[i][0], ny = y + shifts[i][1];
                if (0 <= nx and nx < m and 0 <= ny and ny < n and heights[nx][ny] == -1) {
                    dq.push_back({nx, ny});
                    heights[nx][ny] = h + 1;
                }
            }
        }
        return heights;
    }
};
