from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges, n, src, dst):
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        dist = [10**9] * (n + 1)
        dist[src] = 0

        q = deque([src])

        while q:
            u = q.popleft()

            for v, cost in graph[u]:
                if dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost

                    if cost == 0:
                        q.appendleft(v)
                    else:
                        q.append(v)

        return -1 if dist[dst] == 10**9 else dist[dst]
