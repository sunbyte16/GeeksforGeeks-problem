class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [0] * V

        # Relax all edges V-1 times
        for _ in range(V - 1):
            updated = False

            for u, v, wt in edges:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    updated = True

            # If no update happened, no negative cycle exists
            if not updated:
                break

        # One more relaxation:
        # If an edge can still be relaxed, negative cycle exists.
        for u, v, wt in edges:
            if dist[u] + wt < dist[v]:
                return True

        return False
