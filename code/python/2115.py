# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        set_supply = set(supplies)
        graph = {}
        indegree = {recipe: 0 for recipe in recipes}
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in set_supply:
                    indegree[recipe] += 1
                    graph.setdefault(ingredient, []).append(recipe)
        queue = deque()
        for recipe in recipes:
            if indegree[recipe] == 0:
                queue.append(recipe)        
        res = []
        while queue:
            curr_recipe = queue.popleft()
            res.append(curr_recipe)
            set_supply.add(curr_recipe)
            for dependent in graph.get(curr_recipe, []):
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)        
        return res
