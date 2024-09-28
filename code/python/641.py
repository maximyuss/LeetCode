# https://leetcode.com/problems/design-circular-deque/
class MyCircularDeque:
    def change_index(self, idx: int, direction: int = 1) -> int:
        return (idx + direction) % self.size

    def __init__(self, k: int):
        self.store = [0] * k
        self.count = 0
        self.size = k
        self.begin = 1
        self.end = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.begin = self.change_index(self.begin, -1)
        self.store[self.begin] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.end = self.change_index(self.end)
        self.store[self.end] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.begin = self.change_index(self.begin)
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.end = self.change_index(self.end, -1)
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.store[self.begin]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.store[self.end]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
