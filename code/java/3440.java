# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
class Solution {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        int n = startTime.length,
            gaps[] = new int[n + 1];
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++)
            gaps[i] = startTime[i] - endTime[i - 1];
        gaps[n] = eventTime - endTime[n - 1];
        n++;
        int[] pref = new int[n], suff = new int[n];
        pref[0] = -1; suff[n-1] = -1;
        for (int i = 0; i < n - 1; i++) {
            pref[i + 1] = Math.max(pref[i], gaps[i]);
            int j = n - i - 1;
            suff[j - 1] = Math.max(suff[j], gaps[j]);
        }
        int res = 0;
        for (int i = 0; i < n - 1; i++) {
            int slot = endTime[i] - startTime[i],
                time = gaps[i] + gaps[i + 1];
            if (pref[i] >= slot || suff[i + 1] >= slot)
                time += slot;
            res = Math.max(res, time);
        }
        return res;
    }
}
