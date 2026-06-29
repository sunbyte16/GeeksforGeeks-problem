class Solution:
    def maxDotProduct(self, a, b):
        # code here
        
        dp = [[-1 for i in range(len(b))] for i in range(len(a))]

        def solve(i, j):
            if j == -1:
                return 0
            if i == -1:
                return -10**18
            
            if dp[i][j] != -1: return dp[i][j]
            
            take = (a[i] * b[j]) + solve(i-1, j-1)
            
            skip = solve(i-1, j)
            
            dp[i][j] = max(take,skip)
            
            return dp[i][j]
            
        return solve(len(a) - 1, len(b) - 1)
