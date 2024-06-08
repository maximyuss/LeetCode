//https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        size_t n = arr.size() - 1, l = 0, r = n, mid;
        while (l < r) {
            mid = (l + r) / 2;
            if (arr[mid] < arr[mid + 1])
                l = mid;
            else if (arr[mid - 1] > arr[mid])
                r = mid;
            else
                return mid;
        }
        return -1;
    }
};
