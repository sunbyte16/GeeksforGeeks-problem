class Solution:
    def totalWays(self, arr, target):
        total_sum = sum(arr)
        
        # Edge cases
        if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        S1 = (target + total_sum) // 2
        
        # DP array
        dp = [0] * (S1 + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(S1, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[S1]
