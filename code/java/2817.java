// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
class Solution {
    public int minAbsoluteDifference(List<Integer> nums, int x) {
        int res = Integer.MAX_VALUE;
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = x; i < nums.size(); ++i) {
        set.add(nums.get(i - x));
        Integer high = set.ceiling(nums.get(i)), low = set.floor(nums.get(i));
        if (high != null)
            res = Math.min(res, Math.abs(nums.get(i) - high));
        if (low != null)
            res = Math.min(res, Math.abs(nums.get(i) - low));
        }
        return res;
    }
}
