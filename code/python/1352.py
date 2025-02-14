# https://leetcode.com/problems/product-of-the-last-k-numbers/
class ProductOfNumbers:
    def __init__(self):
        self._prod = [1]
        self._total = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
        else:
            self._total *= num
            self._prod.append(self._total)

    def getProduct(self, k: int) -> int:
        n = len(self._prod) - 1
        if k > n:
            return 0
        return self._total // self._prod[n - k]
