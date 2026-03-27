class Solution:
    def maxChocolate(self, grid):
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

        def solve(row, c1, c2):
            # boundary check
            if c1 < 0 or c1 >= m or c2 < 0 or c2 >= m:
                return float('-inf')

            # last row
            if row == n - 1:
                if c1 == c2:
                    return grid[row][c1]
                else:
                    return grid[row][c1] + grid[row][c2]

            if dp[row][c1][c2] != -1:
                return dp[row][c1][c2]

            maxi = 0

            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    value = 0

                    if c1 == c2:
                        value = grid[row][c1]
                    else:
                        value = grid[row][c1] + grid[row][c2]

                    value += solve(row + 1, c1 + d1, c2 + d2)
                    maxi = max(maxi, value)

            dp[row][c1][c2] = maxi
            return maxi

        return solve(0, 0, m - 1)
