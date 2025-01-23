// https://leetcode.com/problems/count-servers-that-communicate/
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        size_t m = grid.size(), n = grid[0].size(), cnt = 0;
        vector<size_t> rows(n, 0), cols(m, 0);
        for (size_t i = 0; i != m; i++)
            for (size_t j = 0; j != n; j++)
                if (grid[i][j] == 1) {
                        cnt++;
                        cols[i]++;
                        rows[j]++;
                    }
        for (size_t i = 0; i != m; i++) {
            if (cols[i] != 1) continue;
            for (size_t j = 0; j != n; j++)
                if (grid[i][j] == 1 and rows[j] == 1)
                    cnt--;
        }
        return cnt;
    }
};
