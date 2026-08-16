from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        target = n * n

        # jump[i] = destination after landing on i
        jump = list(range(target + 1))

        # Ladders
        for i in range(0, len(lad), 2):
            start = lad[i]
            end = lad[i + 1]
            jump[start] = end

        # Snakes
        for i in range(0, len(sn), 2):
            start = sn[i]
            end = sn[i + 1]
            jump[start] = end

        # BFS
        dist = [-1] * (target + 1)
        dist[1] = 0

        q = deque([1])

        while q:
            current = q.popleft()

            if current == target:
                return dist[current]

            for dice in range(1, 7):
                nxt = current + dice

                if nxt > target:
                    continue

                # Take snake or ladder immediately
                nxt = jump[nxt]

                if dist[nxt] == -1:
                    dist[nxt] = dist[current] + 1
                    q.append(nxt)

        return -1
