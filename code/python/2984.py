# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
        n_h, n_q = len(heights), len(queries)
        res = [-1] * n_q
        deferred = [[] for _ in range(n_h)]
        pq = []
        for i in range(n_q):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                deferred[b].append((heights[a], i))
        for i in range(n_h):
            for query in deferred[i]:
                heapq.heappush(pq, query)
            while pq and pq[0][0] < heights[i]:
                res[pq[0][1]] = i
                heapq.heappop(pq)
        return res
