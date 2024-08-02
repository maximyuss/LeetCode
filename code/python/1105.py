# https://leetcode.com/problems/filling-bookcase-shelves/
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        res = [float('inf')] * (n + 1)
        res[0] = 0
        for i in range(1, n + 1):
            w = books[i - 1][0]
            h = books[i - 1][1]
            res[i] = res[i - 1] + h
            for j in range(i - 1, -1, -1):
                if w + books[j - 1][0] <= shelfWidth:
                    h = max(h, books[j - 1][1])
                    w += books[j - 1][0]
                    res[i] = min(res[i], res[j - 1] + h)
                else:
                    break
        return res[n]
