class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        # Length 1 intervals (single coin)
        for i in range(n):
            dp[i][i] = arr[i]
        
        # Fill DP for all lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # When picking left
                pick_left = arr[i] + min(
                    dp[i+2][j] if i + 2 <= j else 0,
                    dp[i+1][j-1] if i + 1 <= j - 1 else 0
                )
                
                # When picking right
                pick_right = arr[j] + min(
                    dp[i][j-2] if i <= j - 2 else 0,
                    dp[i+1][j-1] if i + 1 <= j - 1 else 0
                )
                
                dp[i][j] = max(pick_left, pick_right)
        
        return dp[0][n-1]
