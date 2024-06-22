# https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        const int n = nums.size();
        nums.emplace_back(1);
        vector<int> count(n + 1, 1);
        int res = 0, countOdd = 0, countOddW = 0;
        for (int l = 0; l <= n; l++) {
            if (nums[l] & 1) {
                countOdd++;
                if (countOddW == k)
                    res += count[countOdd - k - 1] * count[countOdd - 1];
                else
                    countOddW++;
            } else
                count[countOdd]++;
        }
        return res;
    }
};
