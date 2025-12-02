class Solution:
    def tsp(self, cost):
        n = len(cost)
        if n == 1:
            return 0

        INF = 10**18
        FULL = 1 << n
        # dp[mask][i]: min cost to start at 0, visit all in mask, end at i
        dp = [[INF] * n for _ in range(FULL)]
        dp[1][0] = 0  # only city 0 visited, at city 0

        for mask in range(FULL):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                if dp[mask][i] == INF:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    nxt = mask | (1 << j)
                    dp[nxt][j] = min(dp[nxt][j], dp[mask][i] + cost[i][j])

        fullMask = FULL - 1
        ans = INF
        for i in range(n):
            ans = min(ans, dp[fullMask][i] + cost[i][0])

        return ans
