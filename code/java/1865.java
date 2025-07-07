// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
public class FindSumPairs {
    private final Map<Integer, Integer> freq1;
    private final Map<Integer, Integer> freq2;
    private final List<Integer> keys;
    private final int[] nums2;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.freq1 = new HashMap<>();
        for (int x : nums1)
            freq1.put(x, freq1.getOrDefault(x, 0) + 1);
        this.freq2 = new HashMap<>();
        this.nums2 = nums2;
        for (int x : nums2)
            freq2.put(x, freq2.getOrDefault(x, 0) + 1);
        this.keys = new ArrayList<>(freq1.keySet());
        Collections.sort(this.keys);
    }

    public void add(int index, int val) {
        int oldValue = nums2[index];
        freq2.put(oldValue, freq2.get(oldValue) - 1);
        int newValue = oldValue + val;
        nums2[index] = newValue;
        freq2.put(newValue, freq2.getOrDefault(newValue, 0) + 1);
    }

    public int count(int tot) {
        int result = 0;
        for (int num : keys) {
            if (num >= tot) break;
            result += freq1.get(num) * freq2.getOrDefault(tot - num, 0);
        }
        return result;
    }
}
