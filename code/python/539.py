# https://leetcode.com/problems/minimum-time-difference/
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_set = set()
        time_int = []
        for point in timePoints:
            tmp = int(point[0:2]) * 60 + int(point[3:5])
            if tmp in time_set:
                return 0
            time_set.add(tmp)
            time_int.append(tmp)
        time_int.sort()
        res = 24 * 60 - time_int[-1] + time_int[0]
        for i in range(1, len(time_int)):
            res = min(res, time_int[i] - time_int[i - 1])
        return res
