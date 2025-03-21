# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        res, curr = [], 0
        for dur, last in courses:
            heapq.heappush(res, -dur)
            curr += dur
            if curr > last:
                curr += heapq.heappop(res)
        return len(res)
