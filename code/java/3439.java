// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
class Solution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length, winLen = startTime[0];
        for (int i = 1; i != k; i++)
            winLen += startTime[i] - endTime[i - 1];
        if (k == n) {
            winLen += eventTime - endTime[n - 1];
            return winLen;
        }
        winLen += startTime[k] - endTime[k - 1];
        int winMax = winLen, winStart = 0;
        for (int end = k; end != n - 1; end++) {
            winLen -= startTime[end - k] - winStart;
            winStart = endTime[end - k];
            winLen += startTime[end + 1] - endTime[end];
            if (winLen > winMax) winMax = winLen;
        }
        winLen -= startTime[n - 1 - k] - winStart;
        winLen += eventTime - endTime[n - 1];
        if (winLen > winMax) winMax = winLen;
        return winMax;
    }
}
