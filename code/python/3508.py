# https://leetcode.com/problems/implement-router/
from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.dest_map = defaultdict(lambda: [[], 0])

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if self.memory_limit == 0:
            return False
        p = (source, destination, timestamp)
        if p in self.seen:
            return False
        if len(self.queue) == self.memory_limit:
            s, d, t = self.queue.popleft()
            self.seen.remove((s, d, t))
            self.dest_map[d][1] += 1
        self.queue.append(p)
        self.seen.add(p)
        self.dest_map[destination][0].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        s, d, t = self.queue.popleft()
        self.seen.remove((s, d, t))
        self.dest_map[d][1] += 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts, start_idx = self.dest_map.get(destination, ([], 0))
        l = bisect.bisect_left(ts, startTime, lo=start_idx)
        r = bisect.bisect_right(ts, endTime, lo=start_idx)
        return r - l

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
