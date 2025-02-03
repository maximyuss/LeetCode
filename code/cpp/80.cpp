// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size(), res = 2;
        if (n < 2) return n;
        for (int i = 2; i < nums.size(); i++)
            if (nums[res - 2] != nums[i])
                nums[res++] = nums[i];
        return res;
    }
};
