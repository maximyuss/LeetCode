// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
class Solution {
    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        List<List<Integer>> tree = new ArrayList<>();
        for (int i = 0; i < n; i++) tree.add(new ArrayList<>());
        for (int[] e : edges) {
            tree.get(e[0]).add(e[1]);
            tree.get(e[1]).add(e[0]);
        }
        int[] xor = new int[n], in = new int[n], out = new int[n], time = {0};
        
        dfs(0, -1, nums, tree, xor, in, out, time);
        int total = xor[0], res = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a, b, c;
                if (in[i] < in[j] && out[j] <= out[i]) {
                    a = xor[j];
                    b = xor[i] ^ xor[j];
                    c = total ^ xor[i];
                } else if (in[j] < in[i] && out[i] <= out[j]) {
                    a = xor[i];
                    b = xor[j] ^ xor[i];
                    c = total ^ xor[j];
                } else {
                    a = xor[i];
                    b = xor[j];
                    c = total ^ xor[i] ^ xor[j];
                }
                res = Math.min(res, Math.max(a, Math.max(b, c)) - Math.min(a, Math.min(b, c)));
            }
        }
        return res;
    }

    private void dfs(int node, int parent, int[] nums, List<List<Integer>> tree, int[] xor, int[] in, int[] out, int[] time) {
        in[node] = time[0]++;
        xor[node] = nums[node];
        for (int curr : tree.get(node)) {
            if (curr != parent) {
                dfs(curr, node, nums, tree, xor, in, out, time);
                xor[node] ^= xor[curr];
            }
        }
        out[node] = time[0];
    }
}
