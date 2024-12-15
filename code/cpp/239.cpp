// https://leetcode.com/problems/sliding-window-maximum/
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        size_t n = nums.size(), idx = 0;
        vector<int> res (n - k + 1);
        deque<int> dq;
        for (size_t i = 0; i < nums.size(); i++) {
            int num = nums[i];
            while (!dq.empty() and dq.back() < num)
                dq.pop_back();
            dq.push_back(num);
            if (i >= k and nums[i - k] == dq.front())
                dq.pop_front();
            if (i >= k - 1)
                res[idx++] = dq.front();
        }
        return res;
    }
};
