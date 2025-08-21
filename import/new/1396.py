# https://leetcode.com/problems/design-underground-system
class UndergroundSystem:
    def __init__(self):
        self.checkIns = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkIns[id]
        if (start_station, stationName) not in self.time:
            self.time[(start_station, stationName)] = [t - start_time, 1]
        else:
            total_time, counts = self.time[(start_station, stationName)]
            self.times[(start_station, stationName)] = [total_time + t - start_time, counts + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, counts = self.times[(startStation, endStation)]
        return total_time / counts
