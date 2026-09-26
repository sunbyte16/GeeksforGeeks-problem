from collections import deque

class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        g = [[] for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        ecc = [1] * n
        seen = [False] * n
        dist = [0] * n
        mark = [0] * n
        stamp = 0

        def bfs(start, color):
            nonlocal stamp
            stamp += 1
            q = deque([start])
            mark[start] = stamp
            dist[start] = 0
            far = start

            while q:
                u = q.popleft()

                if dist[u] > dist[far]:
                    far = u

                for v in g[u]:
                    if s[v] == color and mark[v] != stamp:
                        mark[v] = stamp
                        dist[v] = dist[u] + 1
                        q.append(v)

            return far

        for i in range(n):
            if seen[i]:
                continue

            color = s[i]

            # Mark this monochromatic component
            q = deque([i])
            seen[i] = True

            while q:
                u = q.popleft()

                for v in g[u]:
                    if not seen[v] and s[v] == color:
                        seen[v] = True
                        q.append(v)

            # Diameter endpoints of this color component
            a = bfs(i, color)
            b = bfs(a, color)

            # dist[] now contains distances from a
            da = [0] * n
            nodes = [a]
            for u in nodes:
                da[u] = dist[u]
                for v in g[u]:
                    if s[v] == color and da[v] == 0 and v != a:
                        nodes.append(v)

            # Distances from b
            bfs(b, color)

            for u in nodes:
                ecc[u] = max(da[u], dist[u]) + 1

        ans = 1

        # Same-color paths and R -> B paths
        for u in range(n):
            ans = max(ans, ecc[u])

            if s[u] == 'R':
                for v in g[u]:
                    if s[v] == 'B':
                        ans = max(ans, ecc[u] + ecc[v])

        return ans
