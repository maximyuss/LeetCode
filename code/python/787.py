# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for i, (a, b, price) in enumerate(flights):
            graph[a].append((b, price))
        prices = [float('inf')] * n
        prices[src] = 0
        queue = deque([(src, 0)])
        k += 1
        while k > 0 and queue:
            size = len(queue)
            while size > 0:
                cur_node, cur_price = queue.popleft()
                for neighbor, price in graph[cur_node]:
                    new_price = cur_price + price
                    if new_price < prices[neighbor]:
                        prices[neighbor] = new_price
                        queue.append((neighbor, new_price))
                size -= 1
            k -= 1
        return prices[dst] if prices[dst] != float('inf') else -1
