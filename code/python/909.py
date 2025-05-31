# https://leetcode.com/problems/snakes-and-ladders/
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        dq = deque([(1, 0)])  #(cell, rolls)
        visited = set([1])
        n = len(board)
        finish_cell = n * n

        # straighten boustrophedon matix
        for i in range(n - 2, -1, -2):
            board[i].reverse()
        board.reverse()

        # bfs
        while dq:
            curr, rolls = dq.popleft()
            for i in range(curr + 1, min(finish_cell + 1, curr + 7)):
                next = i
                cell = board[(next - 1) // n][(next - 1) % n]
                if  cell != -1:
                    next = cell
                if next not in visited:
                    if next == finish_cell:
                        return rolls + 1
                    else:
                        visited.add(next)
                        dq.append((next, rolls + 1))
        return -1
