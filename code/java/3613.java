// https://leetcode.com/problems/minimize-maximum-component-cost/
class Solution {
    private static int[] f;

    private int find(int x) {
        while (x != f[x])
            x = f[x];
        return x;
    }

    private boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        f[x] = y;
        return true;
    }

    public int minCost(int n, int[][] edges, int k) {
        if (n <= k) return 0;
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        int cnt = n;
        f = new int[n];
        for (int i = 0; i < n; i++)
            f[i] = i;
        for (var edge : edges) {
            if (union(edge[0], edge[1])) cnt--;
            if (cnt <= k)  return edge[2];
        }
        return 0;
    }
}
