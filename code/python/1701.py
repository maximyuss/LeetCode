# https://leetcode.com/problems/average-waiting-time/
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = now = 0
        for arrival, time in customers:
            if now > arrival:
                total_time += now - arrival + time
                now += time
            else:
                total_time += time
                now = arrival + time
        return total_time / len(customers)
