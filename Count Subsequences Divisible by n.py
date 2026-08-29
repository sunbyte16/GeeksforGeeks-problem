class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 1000000007
        dp = [0] * n

        for ch in s:
            digit = ord(ch) - ord('0')
            new_dp = dp[:]

            # Start a new subsequence
            new_dp[digit % n] = (new_dp[digit % n] + 1) % MOD

            # Append current digit to existing subsequences
            for r in range(n):
                if dp[r] != 0:
                    nr = (r * 10 + digit) % n
                    new_dp[nr] = (new_dp[nr] + dp[r]) % MOD

            dp = new_dp

        return dp[0]
