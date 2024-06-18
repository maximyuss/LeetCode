#https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
class Solution {
public:
    int binSearch(vector<int>& potions, size_t target) {
        size_t l = 0, m, n = potions.size(), r = n;
        while (l < r) {
            m = (l + r) / 2;
            if (potions[m] >= target)
                r = m;
            else
                l = m + 1;
        }
        return n - l;
    }

    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        size_t n = spells.size();
        vector<int> res;
        res.reserve(n);
        sort(potions.begin(), potions.end());
        for (int spell: spells) {
            res.emplace_back(binSearch(potions, (success + spell - 1) / spell));
        }
        return res;
    }
};

static int speedup=[](){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	return 0;
}();
