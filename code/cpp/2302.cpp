// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        size_t n = nums.size(), left = 0;
        long long total = 0, cnt = 0;
        for (size_t right = 0; right < n; right++) {
            total += nums[right];
            while (total * (right - left + 1) >= k) {
                total -= nums[left];
                left++;
            }
            cnt += (right - left + 1);
        }
        return cnt;
    }
};
