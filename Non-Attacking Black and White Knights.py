class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        total = (n * m) * (n * m - 1)
        attacks = 0

        dx = [1, 2, 2, 1]
        dy = [2, 1, -1, -2]

        for i in range(n):
            for j in range(m):
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        attacks += 1

        return total - attacks * 2
