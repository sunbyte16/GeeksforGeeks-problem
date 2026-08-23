from collections import deque

class Solution:
    def numberOfCells(self, r, c, u, d, mat):
        # code here
        n, m = len(mat), len(mat[0])

        if mat[r][c] == '#':
            return 0

        dist = [[10**9] * m for _ in range(n)]
        dist[r][c] = 0

        q = deque([(r, c)])

        while q:
            x, y = q.popleft()

            for dx, dy, cost in [(0,1,0),(0,-1,0),(-1,0,1),(1,0,0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == '.':
                    nd = dist[x][y] + cost

                    if nd < dist[nx][ny] and nd <= u:
                        dist[nx][ny] = nd
                        if cost:
                            q.append((nx, ny))
                        else:
                            q.appendleft((nx, ny))

        ans = 0

        for i in range(n):
            for j in range(m):
                if dist[i][j] <= u:
                    down = dist[i][j] + i - r
                    if down <= d:
                        ans += 1

        return ans
