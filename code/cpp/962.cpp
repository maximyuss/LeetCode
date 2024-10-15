//https://leetcode.com/problems/maximum-width-ramp/
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        stack<int> st;
        int n = nums.size(), res = 0;
        st.push(0);
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[st.top()])
                st.push(i);
        }
        for (int i = n - 1; i != 0; i--) {
            while (!st.empty() && nums[st.top()] <= nums[i]) {
                res = max(res, i - st.top());
                st.pop();
            }
            if (st.empty()) break;
        }
        return res;
    }
};
