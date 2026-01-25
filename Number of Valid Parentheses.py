class Solution:
    def findWays(self, n):
        if n % 2 == 1:
            return 0
        
        pairs = n // 2
        
        dp = [0] * (pairs + 1)
        dp[0] = 1
        
        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[pairs]
