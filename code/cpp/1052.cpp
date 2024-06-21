// https://leetcode.com/problems/grumpy-bookstore-owner/
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
    	size_t l = 0, r = minutes, n = customers.size(),
    		countSatisfied = 0, countSatisfiedGrumpy = 0, maxSatisfiedGrumpy = 0;
    	for (size_t i = 0; i < n; i++) {
    		countSatisfied += customers[i] * !grumpy[i];
    		if (i < minutes)
    			countSatisfiedGrumpy += customers[i] * grumpy[i];
    	}
    	maxSatisfiedGrumpy = max(maxSatisfiedGrumpy, countSatisfiedGrumpy);
    	while (r < n) {
    		countSatisfiedGrumpy += customers[r] * grumpy[r];
    		countSatisfiedGrumpy -= customers[l] * grumpy[l];
    		maxSatisfiedGrumpy = max(maxSatisfiedGrumpy, countSatisfiedGrumpy);
    		l++; r++;
    	}
    	return countSatisfied + maxSatisfiedGrumpy;
    }
};
