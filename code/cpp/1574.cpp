// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size(), r = n - 1;
        while (r > 0 and arr[r] >= arr[r - 1])
            r--;
        int res = r, l = 0;
        while (l < r and (l == 0 or arr[l - 1] <= arr[l])) {
            while (r < n and arr[l] > arr[r])
                r++;
            res = min(res, r - l - 1);
            l++;
        }
        return res;
    }
};
