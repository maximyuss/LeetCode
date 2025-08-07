// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
class Solution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int left = 0, sum = 0, res = 0;
        for (int right = 0; right < fruits.length; right++) {
            sum += fruits[right][1];
            while (left <= right && minSteps(fruits[left][0], fruits[right][0], startPos) > k) {
                sum -= fruits[left][1];
                left++;
            }
            res = Math.max(res, sum);
        }
        return res;
    }

    private int minSteps(int left, int right, int start) {
        int goLeft = Math.abs(start - left) + (right - left);
        int goRight = Math.abs(start - right) + (right - left);
        return Math.min(goLeft, goRight);
    }
}
