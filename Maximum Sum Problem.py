class Solution:
    def maxSum(self, n,memo = {}):
        # code here
        
        if n in memo:
            return memo[n]
        
        if n == 0:
            return 0
            
        msv = max(n, self.maxSum(n//2,memo) + self.maxSum(n//3,memo) + self.maxSum(n//4,memo))
        memo[n] = msv
        
        return msv
