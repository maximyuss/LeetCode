# https://leetcode.com/problems/count-days-without-meetings/
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        today = 0
        for start, end in meetings:
            if end <= today: 
                continue
            elif start > today: 
                days -= end - start + 1
            else: 
                days -= end - today
            today = end
        return days
