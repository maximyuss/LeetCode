// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
class Solution {
public:
    int minSwaps(string s) {
        size_t count_open = 0, swaps = 0;
        for (int i = 0; i < s.size(); i++)
            if (s[i] == ']')
                if (count_open == 0) {
                    swaps++;
                    count_open++;
                } else
                    count_open--;
            else
                count_open++;
        return swaps;
    }
};
