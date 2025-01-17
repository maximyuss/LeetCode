// https://leetcode.com/problems/neighboring-bitwise-xor/
class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int cur = 1;
        for (size_t i = 0; i < derived.size(); i++)
            cur ^= derived[i];
        return cur;
    }
};
