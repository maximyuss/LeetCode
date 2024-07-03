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
    
    // First version - using my function
    int minDifference(vector<int>& nums) {
        if (nums.size() < 5) return 0;
        
        vector<int> small = findNMinsOrMaxs(MIN, nums, 4);
        vector<int> big = findNMinsOrMaxs(MAX, nums, 4);
        
        int min_diff = INT_MAX;
        for (size_t i = 0; i < 4; i++)
            min_diff = min(min_diff, big[i] - small[i]);
        return min_diff;
    }

    // Second version - using nth_element
    int minDifference_v2(vector<int>& nums) {
    	int n = nums.size();
    	if (n < 5) return 0;
        
    	nth_element(nums.begin(), nums.begin() + 4, nums.end());
    	vector<int> small(nums.begin(), nums.begin() + 4);
    	sort(small.begin(), small.end());
        
    	nth_element(nums.begin(), nums.begin() + 4, nums.end(), greater<int>());
    	vector<int> big(nums.begin(), nums.begin() + 4);
    	sort(big.begin(), big.end());
    
    	int min_diff = INT_MAX;
    	for (size_t i = 0; i < 4; i++)
    		min_diff = min(min_diff, big[i] - small[i]);
    	return min_diff;
    }
};
