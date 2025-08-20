# https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        self.is_even = True

    def addNum(self, num: int) -> None:
        if self.is_even:
            heappush(self.right, num)
            heappush(self.left, -heappop(self.right))
        else:
            heappush(self.left, -num)
            heappush(self.right, -heappop(self.left))
        self.is_even = not self.is_even

    def findMedian(self) -> float:
        if self.is_even:
            return (self.right[0] - self.left[0]) / 2
        else:
            return -self.left[0]
