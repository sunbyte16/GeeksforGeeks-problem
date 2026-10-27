class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        dp = [0]*(n+1)

        for i in range(n):
            dp[i+1] = dp[i] + 1
            if i == 0:
                continue

            dp[i+1] = max(dp[i+1], dp[i-1] + 4 - int(s[i] == s[i-1]))

        return dp[-1]
