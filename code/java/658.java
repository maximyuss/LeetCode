// https://leetcode.com/problems/find-k-closest-elements
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int l = 0, r = arr.length - k, m;
        while (l < r) {
            m = (l + r) / 2;
            if (x - arr[m] > arr[m + k] - x)
                l = m + 1;
            else
                r = m;
        }
        Integer[] res = new Integer[k];
        for (int i = 0; i < k; i++)
            res[i] = arr[l + i];
        return Arrays.asList(res);
    }
}
