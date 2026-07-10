class Solution:
    def solve(self, visited, matrix, x, y, xd, yd, length):
        #code here
        if x == xd and y == yd:
            self.maxi = max(self.maxi, length)
            return

        visited[x][y] = 1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.n and 0 <= ny < self.m and
                not visited[nx][ny] and matrix[nx][ny] != 0):
                self.solve(visited, matrix, nx, ny, xd, yd, length + 1)

        visited[x][y] = 0

    def longestPath(self, mat, xs, ys, xd, yd):
        self.n, self.m = len(mat), len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        self.maxi = -1
        visited = [[0] * self.m for _ in range(self.n)]

        self.solve(visited, mat, xs, ys, xd, yd, 0)
        return self.maxi
