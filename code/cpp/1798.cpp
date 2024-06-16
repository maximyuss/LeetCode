//https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        size_t sum = 1;
        sort(coins.begin(), coins.end());
        for (size_t i = 0; i < coins.size(); i++) {
            if (sum < coins[i]) break;
            sum += coins[i];
        }
        return sum;
    }
};
