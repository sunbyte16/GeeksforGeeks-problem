class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        dp = [10**9] * (x + l + 1)
        dp[0] = 0

        for i in range(1, x + l + 1):
            if i >= s:
                dp[i] = min(dp[i], dp[i - s] + cs)
            if i >= m:
                dp[i] = min(dp[i], dp[i - m] + cm)
            if i >= l:
                dp[i] = min(dp[i], dp[i - l] + cl)

        return min(dp[x:])
