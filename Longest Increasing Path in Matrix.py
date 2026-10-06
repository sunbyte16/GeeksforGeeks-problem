class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        dist = [[-1]*m for _ in range(n)]

        def dfs(r, c):
            nonlocal dist, m, n
            if dist[r][c] != -1:
                return dist[r][c]

            d = 1
            for r0, c0 in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if r0 < 0 or r0 >= n or c0 < 0 or c0 >= m:
                    continue
                if matrix[r0][c0] > matrix[r][c]:
                    d = max(d, dfs(r0, c0)+1)
            dist[r][c] = d
            return d

        ans = 0
        for r in range(n):
            for c in range(m):
                if dist[r][c] == -1:
                    ans = max(ans, dfs(r, c))
        return ans
