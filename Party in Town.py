from collections import deque

class Solution:
    def partyHouse(self, adj):
        def bfs(start):
            n = len(adj)
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            farthest = start

            while q:
                node = q.popleft()

                for x in adj[node]:
                    x -= 1

                    if dist[x] == -1:
                        dist[x] = dist[node] + 1
                        q.append(x)

                        if dist[x] > dist[farthest]:
                            farthest = x

            return farthest, dist[farthest]

        diameter_end, _ = bfs(0)
        _, diameter = bfs(diameter_end)

        return (diameter + 1) // 2
