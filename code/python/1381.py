# https://leetcode.com/problems/design-a-stack-with-increment-operation/
# List using Lazy Propagation
class CustomStack:
    def __init__(self, maxSize: int):
        self.storage = [0] * maxSize
        self.inc = [0] * maxSize
        self.top = -1
        self.size = maxSize

    def push(self, x: int) -> None:
        if self.top + 1 < self.size:
            self.top += 1
            self.storage[self.top] = x

    def pop(self) -> int:
        if self.top == -1: return -1
        top = self.top
        res = self.storage[self.top] + self.inc[top]
        if top > 0:
            self.inc[top - 1] += self.inc[top]
        self.inc[top] = 0
        self.top -= 1
        return res

    def increment(self, k: int, val: int) -> None:
        if self.top != -1:
            idx = min(self.top, k - 1)
            self.inc[idx] += val
