// https://leetcode.com/problems/rearranging-fruits/
class Solution {
    public long minCost(int[] basket1, int[] basket2) {
                Map<Integer, Integer> freq = new HashMap<>();
        for (int x : basket1)
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        for (int x : basket2)
            freq.put(x, freq.getOrDefault(x, 0) - 1);

        List<Integer> exchange = new ArrayList<>();
        int min = Math.min(basket1[0], basket2[0]);
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int fruit = entry.getKey();
            int cnt = entry.getValue();
            if (cnt % 2 != 0) return -1;
            for (int i = 0; i < Math.abs(cnt) / 2; i++) {
                exchange.add(fruit);
            }
            min = Math.min(min, fruit);
        }
        Collections.sort(exchange);
        long res = 0;
        min <<= 1;
        for (int i = 0; i < exchange.size() / 2; i++)
            res += Math.min(min, exchange.get(i));
        return res;
    }
}
