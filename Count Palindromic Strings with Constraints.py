class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 1000000007
        ans = 0

        # perm = P(k, m) = k * (k-1) * ... * (k-m+1)
        perm = 1

        for m in range(0, k + 1):
            if m > 0:
                perm = perm * (k - m + 1) % MOD

            # Even length = 2*m
            # Left half contains m distinct characters.
            if m >= 1 and 2 * m <= n:
                ans = (ans + perm) % MOD

            # Odd length = 2*m + 1
            # m characters occur twice, center must be a different character.
            if 2 * m + 1 <= n and m < k:
                odd_count = perm * (k - m) % MOD
                ans = (ans + odd_count) % MOD

        return ans
