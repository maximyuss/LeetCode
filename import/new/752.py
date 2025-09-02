# https://leetcode.com/problems/open-the-lock/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends: return -1
        dq = deque([('0000', 0)])
        seen = set('0000')
        while dq:
            curr, moves = dq.popleft()
            if curr == target:
                return moves
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(curr[i]) + delta) % 10
                    new_ = curr[:i] + str(new_digit) + curr[i+1:]
                    if new_ not in seen and new_ not in deadends:
                        seen.add(new_)
                        dq.append((new_, moves + 1))
        return -1
