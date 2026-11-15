class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        n = len(s)

        digit_sum = sum(int(ch) for ch in s)

        return (digit_sum * pow(2, n - 1, MOD)) % MOD
