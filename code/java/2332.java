// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
class Solution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Arrays.sort(buses);
        Arrays.sort(passengers);
        int n = passengers.length, i = 0, cnt = 0;
        for (int timeBus : buses) {
            cnt = capacity;
            while (i < n && passengers[i] <= timeBus && cnt > 0) {
                i++;
                cnt--;
            }
        }
        int res = (cnt > 0) ? buses[buses.length - 1] : passengers[i - 1];
        for (int j = i - 1; j >= 0; j--)
            if (passengers[j] == res)
                res--;
            else
                break;
        return res;
    }
}
