# https://leetcode.com/problems/peeking-iterator/
class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.next_elem = None
        self.peeked = False

    def peek(self):
        if not self.peeked:
            if self.iterator.hasNext():
                self.next_elem = self.iterator.next()
                self.peeked = True
        return self.next_elem

    def next(self):
        if self.peeked:
            self.peeked = False
            return self.next_elem
        elif self.iterator.hasNext():
            return self.iterator.next()

    def hasNext(self):
        return self.peeked or self.iterator.hasNext()
