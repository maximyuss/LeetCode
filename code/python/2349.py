# https://leetcode.com/problems/design-a-number-container-system/
class NumberContainers:
    def __init__(self):
        self.idx_num = {}
        self.num_idx = {}

    def change(self, index: int, number: int) -> None:
        self.idx_num[index] = number
        if number not in self.num_idx:
            self.num_idx[number] = []
        heapq.heappush(self.num_idx[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_idx:
            return -1
        while self.num_idx[number]:
            cur = self.num_idx[number][0]
            if self.idx_num[cur] == number:
                return cur
            heapq.heappop(self.num_idx[number])
        return -1
