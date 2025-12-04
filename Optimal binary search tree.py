class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        
        # Precompute prefix sums of frequencies for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + freq[i]
        
        # dp[i][j] = min cost for keys[i..j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single key
        for i in range(n):
            dp[i][i] = freq[i]
        
        # Fill DP table for chains of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                fsum = prefix[j + 1] - prefix[i]
                dp[i][j] = float('inf')
                
                # Try each possible root k in range [i, j]
                for k in range(i, j + 1):
                    left_cost = dp[i][k - 1] if k > i else 0
                    right_cost = dp[k + 1][j] if k < j else 0
                    total_cost = left_cost + right_cost + fsum
                    dp[i][j] = min(dp[i][j], total_cost)
        
        return dp[0][n - 1]
