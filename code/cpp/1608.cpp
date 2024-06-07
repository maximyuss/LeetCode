class Solution {
public:
    int count(vector<int>& nums, int target) {
        int res = 0;
        for (int num : nums)
            if (num >= target) res++;
        return res;
    }

    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size(), m, res;
        while (l <= r) {
            m = (l + r) / 2;
            res = count(nums, m);
            if (res == m) return res;
            if (res > m)
                l = m + 1;
            else
                r = m - 1;
        }
        return -1;
    }
};
