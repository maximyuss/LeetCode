// https://leetcode.com/problems/maximal-score-after-applying-k-operations/
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue <int> pq(nums.begin(), nums.end());
        long long res = 0;
        for (size_t i = 0; i < k; i++) {
            int num = pq.top();
            if (num == 1) {
                res += (k - i);
                break;
            }
            pq.pop();
            res += num;
            pq.push((num + 2) / 3);
        }
        return res;
    }
};
