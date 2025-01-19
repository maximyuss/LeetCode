// https://leetcode.com/problems/trapping-rain-water/
class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1, maxL = 0, maxR = 0, res = 0;
        while (l <= r) {
            if (height[l] <= height[r]) {
                if (height[l] >= maxL)
                    maxL = height[l];
                else
                    res += maxL - height[l];
                l++;
            } else {
                if (height[r] >= maxR)
                    maxR = height[r];
                else
                    res += maxR - height[r];
                r--;
            }
        }
        return res;
    }
};
