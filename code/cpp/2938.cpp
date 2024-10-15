// https://leetcode.com/problems/separate-black-and-white-balls/
class Solution {
public:
    long long minimumSteps(string s) {
        long long swaps = 0;
        int whitePosition = 0;
        for (size_t i = 0; i < s.size(); i++)
            if (s[i] == '0') {
                swaps += i - whitePosition;
                whitePosition++;
            }
        return swaps;
    }
};
