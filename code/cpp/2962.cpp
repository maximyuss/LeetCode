// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int max = *max_element(nums.begin(), nums.end()), left = 0;
        long long res = 0;
        for (size_t right = 0; right < nums.size(); right++) {
            if (nums[right] == max)
                k -= 1;
            while (not k) {
                if (nums[left] == max)
                    k++;
                left++;
            }
            res += left;
        }
        return res;
    }
};
