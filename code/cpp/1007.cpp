// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution {
public:
    int check(const auto& tops, const auto& bottoms, int target) {
        int swapT = 0, swapB = 0;
        for (size_t i = 0; i != tops.size(); ++i) {
            if (tops[i] != target and bottoms[i] != target)
                return -1;
            else if (tops[i] != target)
                swapT += 1;
            else if (bottoms[i] != target)
                swapB += 1;
        }
        return min(swapT, swapB);
    }

    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int res = check(tops, bottoms, tops[0]);
        if (res != -1)
            return res;
        return check(tops, bottoms, bottoms[0]);
    }
};
