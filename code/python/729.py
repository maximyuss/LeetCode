# https://leetcode.com/problems/my-calendar-i/
from bisect import bisect_left
_MAX_VALUE_ = 10 ** 9 + 1

class MyCalendar2:
    def __init__(self):
        self.store = [(-1, -1), (_MAX_VALUE_, _MAX_VALUE_)]

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.store, (start, end))
        if end > self.store[idx][0]:
            return False
        if start < self.store[idx - 1][1]:
            return False
        self.store.insert(idx, (start, end))
        return True
