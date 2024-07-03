// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution {
public:
    enum typeOfFind { MIN, MAX };
    vector<int> findNMinsOrMaxs(typeOfFind type, vector<int>& nums, int n) {
        priority_queue<int> pq;
        int count = 0, tmp;
        for (int num : nums) {
            if (type == MAX)
                tmp = -num;
            else
                tmp = num;
            if (count < n) {
                pq.push(tmp);
                count++;
            } else if (tmp < pq.top()) {
                pq.pop();
                pq.push(tmp);
            }
        }
        vector<int> res(n);
        if (type == MAX)
            for (size_t i = 0; i < n; i++) {
                res[i] = -pq.top();
                pq.pop();
            }
        else
            for (size_t i = n - 1; i + 1 != 0; i--) {
                res[i] = pq.top();
                pq.pop();
            }
        return res;
    }

    int minDifference(vector<int>& nums) {
        if (nums.size() < 5)
            return 0;
        vector<int> arr, tmp;
        int res = INT_MAX;
        arr = findNMinsOrMaxs(MIN, nums, 4);
        tmp = findNMinsOrMaxs(MAX, nums, 4);
        for (int num : tmp)
            if (num > arr[3])
                arr.push_back(num);
        for (int l = 0, r = arr.size() - 4; l < 4; l++, r++)
            res = min(res, arr[r] - arr[l]);
        return res;
    }
};
