# https://leetcode.com/problems/design-front-middle-back-queue/
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class FrontMiddleBackQueue:
    def __init__(self):
        self.begin = None
        self.end = None
        self.mid = None
        self.count = 0

    def pushFront(self, val: int) -> None:
        self.begin = Node(val, None, self.begin)
        if self.count == 0:
            self.end = self.mid = self.begin
        else:
            self.begin.next.prev = self.begin
            if self.count % 2 == 1:
                self.mid = self.mid.prev
        self.count += 1

    def pushMiddle(self, val: int) -> None:
        if self.count == 0:
            self.begin = self.end = self.mid = Node(val)
        else:
            if self.count % 2 == 1:
                self.mid = Node(val, self.mid.prev, self.mid)
            else:
                self.mid = Node(val, self.mid, self.mid.next)
        if self.count == 1:
            self.begin = self.mid
            self.end.prev = self.mid
        elif self.count > 1:
            self.mid.prev.next = self.mid
            self.mid.next.prev = self.mid
        self.count += 1

    def pushBack(self, val: int) -> None:
        self.end = Node(val, self.end)
        if self.count == 0:
            self.begin = self.mid = self.end
        else:
            self.end.prev.next = self.end
            if self.count % 2 == 0:
                self.mid = self.mid.next
        self.count += 1

    def popFront(self) -> int:
        if self.count == 0: return -1
        res = self.begin.val
        if self.count == 1:
            self.begin = self.mid = self.end = None
        else:
            self.begin = self.begin.next
            self.begin.prev = None
            if self.count % 2 == 0:
                self.mid = self.mid.next
        self.count -= 1
        return res

    def popMiddle(self) -> int:
        if self.count == 0: return -1
        res = self.mid.val
        if self.count == 1:
            self.begin = self.mid = self.end = None
        elif self.count == 2:
            self.begin = self.mid = self.end
            self.begin.prev = None
        else:
            self.mid.prev.next = self.mid.next
            self.mid.next.prev = self.mid.prev
            if self.count % 2 == 0:
                self.mid = self.mid.next
            else:
                self.mid = self.mid.prev
        self.count -= 1
        return res

    def popBack(self) -> int:
        if self.count == 0: return -1
        res = self.end.val
        if self.count == 1:
            self.begin = self.mid = self.end = None
        else:
            self.end = self.end.prev
            self.end.next=None
            if self.count % 2 == 1:
                self.mid = self.mid.prev
        self.count -= 1
        return res
