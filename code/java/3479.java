// https://leetcode.com/problems/fruits-into-baskets-iii/
class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = baskets.length, res = 0;
        int size = Math.max(1, Integer.highestOneBit(n - 1) << 1);  
        int[] tree = new int[size << 1];
        for (int i = 0; i < n; i++)
            tree[size + i] = baskets[i];
        for (int i = size - 1; i > 0; i--)
            tree[i] = Math.max(tree[i << 1], tree[i << 1 | 1]);

        for (int fruit : fruits) {
            if (tree[1] < fruit) {
                res++;
                continue;
            }
            int node = 1;
            while (node < size) {
                int left = tree[node << 1];
                node = (left >= fruit) ? (node << 1) : (node << 1 | 1);
            }
            tree[node] = 0;
            for (node >>= 1; node > 0; node >>= 1)
                tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
        }
        return res;
    }
}
