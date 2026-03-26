import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7

        # Build graph
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Distance and ways arrays
        dist = [float('inf')] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    ways[v] = ways[u]
                    heapq.heappush(pq, (new_dist, v))

                elif new_dist == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[V - 1] % MOD
