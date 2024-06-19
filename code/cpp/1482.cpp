//https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution {
public:
    bool countBlooms(vector<int>& bloomDay, int m, int k, int day) {
        size_t i = 0, count = 0;
        for (int e : bloomDay) {
            if (e<= day) {
                i++;
                if (i == k) {
                    count++;
                    if (count == m) return true;
                    i = 0;
                }
            }
            else
                i = 0;
        }
        return false;
    }

    int minDays(vector<int>& bloomDay, int m, int k) {
        size_t target = (size_t)m * k;
        if (target > bloomDay.size()) return -1;
        size_t l = 1, mid, r = 1e9;
        while (l < r) {
            mid = (l + r) / 2;
            if (countBlooms(bloomDay, m, k, mid))
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
};

static int speedup=[](){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	return 0;
}();
