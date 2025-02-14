# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.store = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        self.store.append((val, min_val))

    def pop(self) -> None:
        self.store.pop()

    def top(self) -> int:
        return self.store[-1][0] if self.store else None

    def getMin(self) -> int:
        return self.store[-1][1] if self.store else None
