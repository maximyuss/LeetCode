# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        def find(day): // Union-Find search function
            while next_day[day] != day:
                next_day[day] = next_day[next_day[day]]
                day = next_day[day]
            return day

        events.sort(key=lambda x: x[1])
        next_day = [x for x in range(events[len(events) - 1][1] + 2)] // Initialize disjoint set
        res = 0
        for start, end in events:
            day = find(start)
            if day <= end:
                res += 1
                next_day[day] = find(day + 1)
        return res
