// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
class Solution {
    int search(int[] nextDay, int day) {
        // Union-Find search function
        while (nextDay[day] != day) {
            nextDay[day] = nextDay[nextDay[day]];
            day = nextDay[day];
        }
        return day;
    }

    public int maxEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[1] - b[1]);
        // Initialize disjoint set
        int[] nextDay = new int[events[events.length - 1][1] + 2];
        for (int d = 0; d < nextDay.length; d++)
            nextDay[d] = d;

        int res = 0;
        for (int[] event : events) {
            int day = search(nextDay, event[0]);
            if (day <= event[1]) {
                res++;
                nextDay[day] = search(nextDay, day + 1);
            }
        }
        return res;
    }
}
