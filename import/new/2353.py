# https://leetcode.com/problems/design-a-food-rating-system/
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.raitings = {}
        self.foods = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            self.raitings.setdefault(cuisine, []).append((-rating, food))
        for cuisine in self.raitings:
            heapify(self.raitings[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        if self.foods[food][1] == newRating: return
        cuisine = self.foods[food][1]
        self.foods[food] = (newRating, cuisine)
        heappush(self.raitings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.raitings[cuisine][0][0] != -self.foods[self.raitings[cuisine][0][1]][0]:
            heappop(self.raitings[cuisine])
        return self.raitings[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
