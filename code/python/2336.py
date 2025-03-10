# https://leetcode.com/problems/smallest-number-in-infinite-set/
class SmallestInfiniteSet:
    def __init__(self):
        self.set = set()
        self.min = 1
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap)
            self.set.remove(res)
        else:
            res = self.min
            self.min += 1
        return res

    def addBack(self, num: int) -> None:
        if self.min <= num or num in self.set:
            return
        heapq.heappush(self.heap, num)
        self.set.add(num)
