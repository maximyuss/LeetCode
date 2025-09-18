// https://leetcode.com/problems/generate-schedule/
class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n < 5: return []
        schedule, seen = [], set()
        for d in range(1, n):
            for i in range(2 * (n + 1)):
                a, b = i % n, (i + d) % n
                if (a, b) in seen:
                    continue
                if schedule:
                    u, v = schedule[-1]
                    if a in (u, v) or b in (u, v):
                        continue
                schedule.append([a, b])
                seen.add((a, b))
        return schedule
