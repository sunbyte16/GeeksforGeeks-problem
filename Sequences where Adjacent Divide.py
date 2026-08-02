class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        dp = [1]*(m+1)
        dp[0] = 0
        
        for _ in range(1, n):
            next_dp = [0]*(m+1)
            for i in range(1, m+1):
                for j in range(1, m+1):
                    if i%j == 0 or j%i == 0:
                        next_dp[j] += dp[i]
            dp = next_dp
        
        return sum(dp)
