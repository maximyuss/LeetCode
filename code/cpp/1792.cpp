// https://leetcode.com/problems/maximum-average-pass-ratio/
class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
    	auto calcRatio = [&](double a, double b) { return (a + 1) / (b + 1) - a / b; };
    	priority_queue <pair<double, pair<int, int>>> pq;
    	double ratio, res = 0;
    	int a, b;
    	size_t n = classes.size();
    	for (size_t i = 0; i < n; i++) {
    		a = classes[i][0], b = classes[i][1];
    		res += (double)a / b;
    		pq.push({ calcRatio(a, b), {a, b} });
    	}
    	for (size_t i = 0; i < extraStudents; i++) {
    		auto [ratio, ele] = pq.top();
    		pq.pop();
    		a = ele.first + 1, b = ele.second + 1;
    		res += ratio;
    		pq.push({ calcRatio(a, b), {a, b} });
    	}
    	return res / n;
    }
};
