from collections import deque

class Solution:
    def shortestPath(self, mat):
        n = len(mat)
        m = len(mat[0])

        safe = [row[:] for row in mat]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Mark landmines and adjacent cells unsafe
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    safe[i][j] = 0
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m:
                            safe[x][y] = 0

        q = deque()

        # Start from every safe cell in first column
        for i in range(n):
            if safe[i][0] == 1:
                q.append((i, 0, 1))
                safe[i][0] = 0

        # BFS
        while q:
            x, y, dist = q.popleft()

            if y == m - 1:
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and safe[nx][ny] == 1:
                    safe[nx][ny] = 0
                    q.append((nx, ny, dist + 1))

        return -1
