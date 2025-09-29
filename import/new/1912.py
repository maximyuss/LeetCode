# https://leetcode.com/problems/design-movie-rental-system/
class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.price = {}
        self.available = {}
        self.rented = SortedList()
        for s, m, p in entries:
            self.price[(s, m)] = p
            if m not in self.available:
                self.available[m] = SortedList()
            self.available[m].add((p, s))

    def search(self, movie: int) -> list[int]:
        if movie not in self.available:
            return []
        return [s for _, s in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.available[movie].discard((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.rented.discard((p, shop, movie))
        self.available[movie].add((p, shop))

    def report(self) -> list[list[int]]:
        return [[s, m] for p, s, m in self.rented[:5]]
        
