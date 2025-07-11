// https://leetcode.com/problems/meeting-rooms-iii/
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        long[] availableTime = new long[n];
        int[] freq = new int[n];
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        for (int[] meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            long minAvailableTime = Long.MAX_VALUE;
            int minRoom = 0;
            boolean foundRoom = false;
            for (int i = 0; i < n; i++) {
                if (availableTime[i] <= start) {
                    availableTime[i] = end;
                    freq[i]++;
                    foundRoom = true;
                    break;
                }
                if (availableTime[i] < minAvailableTime) {
                    minAvailableTime = availableTime[i];
                    minRoom = i;
                }
            }
            if (!foundRoom) {
                availableTime[minRoom] += end - start;
                freq[minRoom]++;
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++)
            if (freq[i] > freq[res])
                res = i;
        return res;
    }
}
