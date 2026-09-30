class Solution:
    def ways(self, x: int, y: int) -> int:
        MOD = 10**9 + 7
        n = x + y
        
        # C(x+y, x)
        ans = 1
        for i in range(1, min(x, y) + 1):
            ans = ans * (n - i + 1) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD
        
        return ans
