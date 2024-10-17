//https://leetcode.com/problems/maximum-swap/
class Solution {
public:
    int maximumSwap(int num) {
        string digits = to_string(num);
        int n = digits.size(), idx_max = n - 1, idx_swap1 = -1, idx_swap2 = -1;
        for (int i = n - 2; i >= 0; i--) {
            if (digits[i] > digits[idx_max])
                idx_max = i;
            else if (digits[i] < digits[idx_max]) {
                idx_swap1 = i;
                idx_swap2 = idx_max;
            }
        }
        if (idx_swap1 != -1 and idx_swap2 != -1)
            swap(digits[idx_swap1], digits[idx_swap2]);
        return stoi(digits);
    }
};
